from fastapi import FastAPI, HTTPException
import comet_ml
from comet_ml import API
from comet_ml.integration.sklearn import load_model, log_model
import pandas as pd
from pydantic import BaseModel


app = FastAPI()

# Clé API et informations du modèle
COMET_API_KEY = "6l3PPIsKeGgBrUF4d5Lv0XKmW"
WORKSPACE = "justrunnz"
MODEL_NAME = "diabetes-predict-model"
MODEL_VERSION = "1.2.0"

comet_ml.login()

loaded_model = load_model("registry://justrunnz/diabetes-predict-model")



class InputData(BaseModel):
    gender: int
    hypertension: int
    heart_disease: int
    age: float
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
def predict(data: InputData):
    data_dict = data.dict()
    new_data = pd.DataFrame([data_dict])
    prediction = loaded_model.predict(new_data)
    if prediction[0] == 1:
        return {"prediction": "The patient is likely to have diabetes"}
    else:
        return {"prediction": "The patient is not likely to have diabetes"}
    
    
# @app.get('/test')
# def test():
#     experiment = comet_ml.start(experiment_key="ae0f79f9b30343de850bc40de6f9acbf")



#     new_data = pd.DataFrame({
#         'gender': [0],
#         'hypertension': [0],
#         'heart_disease': [0],
#         'age': [50.0],
#         'bmi': [25.0],
#         'HbA1c_level': [600.0],
#         'blood_glucose_level': [100]
#     })

#     prediction = loaded_model.predict(new_data)
#     print(prediction)