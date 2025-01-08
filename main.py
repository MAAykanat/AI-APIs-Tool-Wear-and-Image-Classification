from fastapi import FastAPI, Depends, Request
from models import RequestCNCMachine, UpdateCNCMachine

import numpy as np

from helpers import predict_tool_wear, insert_machine_status
from config import estimator_toolwear
from database import create_db_and_tables, get_db
from sqlmodel import Session


app = FastAPI()

# Creates all the tables defined in models module
create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define the endpoint for the prediction
@app.post("/predict/toolwear")
async def predict_tool_wear_status(request: RequestCNCMachine):
    prediction = predict_tool_wear(estimator_toolwear, request.dict())
    
    # Convert numpy types to native Python types
    if isinstance(prediction, np.ndarray):
        prediction = prediction.tolist()
    elif isinstance(prediction, np.int64):
        prediction = int(prediction)
    elif isinstance(prediction, np.float64):
        prediction = float(prediction)

    return prediction

# Define the endpoint for the prediction and insert result into the database
@app.post("/predict_and_insert/toolwear")
async def predict_tool_wear_and_insert(request: RequestCNCMachine, fastapi_req:Request, db: Session = Depends(get_db)):
    prediction = predict_tool_wear(estimator_toolwear, request.dict())
    
    # Convert numpy types to native Python types
    if isinstance(prediction, np.ndarray):
        prediction = prediction.tolist()
    elif isinstance(prediction, np.int64):
        prediction = int(prediction)
    elif isinstance(prediction, np.float64):
        prediction = float(prediction)
    
    # Insert the prediction into the database
    db_insert_record = insert_machine_status(request=request.dict(), prediction=prediction,
                                          client_ip=fastapi_req.client.host,
                                          db=db)
    
    return {"prediction": prediction, "db_record": db_insert_record}