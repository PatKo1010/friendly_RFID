from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

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
    time.sleep(3)  
    x="Hello world!"
    return {"message": x}

@app.post("/cloneCardData", )
def cloneCardData(request: CloneCardDataRequest):
    print(request)
    time.sleep(3)
    message = "true"
    return {"result": message}


