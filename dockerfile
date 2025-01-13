# Utiliser l'image officielle de Python comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir fastapi[standard] comet_ml cloudpickle pandas pydantic scikit-learn

# Exposer le port utilisé par FastAPI
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["fastapi", "run"]
