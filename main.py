from fastapi import FastAPI, HTTPException
import comet_ml
from comet_ml import API
from comet_ml.integration.sklearn import load_model, log_model
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    # put all origin
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Clé API et informations du modèle
COMET_API_KEY = "6l3PPIsKeGgBrUF4d5Lv0XKmW"
WORKSPACE = "justrunnz"
MODEL_NAME = "diabetes-predict-model"
MODEL_VERSION = "1.2.0"

comet_ml.login()

loaded_model = load_model("registry://justrunnz/diabetes-predict-model")



class InputData(BaseModel):
    gender: str
    hypertension: bool
    heart_disease: bool
    age: int
    bmi: float
    hba1c_level: float
    blood_glucose_level: int

def check_comet_connection():
    try:
        api = API(api_key=COMET_API_KEY)
        projects = api.get_workspaces()
        return True
    except Exception as e:
        print(f"Erreur de connexion à Comet ML : {e}")
        return False

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/healthcheck")
def healthcheck():
    if check_comet_connection():
        return {"status": "healthy", "message": "API fonctionne correctement, connectée à Comet ML."}
    else:
        raise HTTPException(
            status_code=500,
            detail="Erreur de connexion à Comet ML. Vérifiez votre clé API ou votre réseau."
        )


@app.post("/predict/")
def predict(data: InputData):
    data_dict = data.dict()
    gender = 1 if data_dict['gender'] == 'male' else 0
    hypertension = 1 if data_dict['hypertension'] == True else 0
    heart_disease = 1 if data_dict['heart_disease'] == True else 0
    data_dict['age'] = float(data_dict['age'])
    # new_data = pd.DataFrame([data_dict])
    new_data = pd.DataFrame([
        {
            "gender": gender,
            "hypertension": hypertension,
            "heart_disease": heart_disease,
            "age": data_dict['age'],
            "bmi": data_dict['bmi'],
            "HbA1c_level": data_dict['hba1c_level'],
            "blood_glucose_level": data_dict['blood_glucose_level']
        }
    ])
    prediction = loaded_model.predict(new_data)
    if prediction[0] == 1:
        return {"prediction":  True, "message": "The patient is likely to have diabetes"}
    else:
        return {"prediction": False, "message": "The patient is not likely to have diabetes"}
    