from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/houseAve.do?year=2020&month=11&metroCd=11&cityCd=12&apiKey=0Egqpgz9b2LMuwGWmM2zVozH8J94H2KP4hZYZY7H&returnType=json"

    contents = requests.get(URL).text

    return { "message": contents }

@app.get("/home")
def home():
    return { "message": "Home!" }