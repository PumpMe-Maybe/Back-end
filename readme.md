# API Documentation

Welcome to the API documentation for our application. This guide will provide you with all the necessary information to interact with our API and utilize its features effectively.


## Installation
Install fastapi, cometML : 
```bash
pip install comet_ml "fastapi[standard]"
```
Add the cometML API key to the environment variables:
```bash
export COMET_API_KEY=<your_comet_api_key>
```
Or via a .env file:

## Launch the app
```bash
fastapi dev main.py
```

## Endpoints

The following endpoints are available in our API:

1. POST : `/predict`: Predict if the user has diabetes based on the info he gaves us
2. GET : `/healthcheck` : Check the health of the api, and the connection to comet ML

Please refer to the API documentation for detailed information on each endpoint, including the supported HTTP methods, request parameters, and response examples.

