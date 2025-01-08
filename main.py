from fastapi import FastAPI
from models import CNCMachine

import numpy as np

from helpers import predict_tool_wear
from config import estimator_toolwear

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict/toolwear")
async def predict_tool_wear_status(request: CNCMachine):
    prediction = predict_tool_wear(estimator_toolwear, request.dict())
    
    # Convert numpy types to native Python types
    if isinstance(prediction, np.ndarray):
        prediction = prediction.tolist()
    elif isinstance(prediction, np.int64):
        prediction = int(prediction)
    elif isinstance(prediction, np.float64):
        prediction = float(prediction)

    return prediction
