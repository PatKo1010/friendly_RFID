from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
import subprocess
import tkinter as tk
import step1
import json,os,glob

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class CloneCardDataRequest(BaseModel):
    key1: str
    key2: str

@app.get("/readCardData")
def readCardData():
    x="Card read sucessfully. Shady stuff commencing"
    time.sleep(3)
    try:
        step1.reads()  
    except Exception as e:
        x=e
    return {"message": x}

@app.post("/cloneCardData", )
def cloneCardData(request: CloneCardDataRequest):
    print(request)
    time.sleep(3)
    message = "true"
    return {"result": message}


