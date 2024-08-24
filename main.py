from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time
import subprocess
import tkinter as tk
import step1
import json,os,glob
import step2

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# class CloneCardDataRequest(BaseModel):
#    key1: str
#    key2: str

@app.get("/readCardData")
def readCardData():
    x="Card read sucessfully. Shady stuff commencing"
    time.sleep(3)
    try:
        step1.reads()  
    except Exception as e:
        x=e.message
    return {"message": x}

@app.get("/cloneCardData")
def cloneCardData():
    x="Card cloned yaaaaaaaaa"
    try:
        step2.clones()
        print("clone done")
    except Exception as e:
        print("error")
        x=e.message
    return {"message": x}


