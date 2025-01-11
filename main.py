from fastapi import FastAPI, Depends, Request, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from models import RequestCNCMachine, UpdateCNCMachine

import numpy as np
import pandas as pd

from helpers import * 
from config import estimator_toolwear, dataset_save_path
from database import create_db_and_tables, get_db
from sqlmodel import Session

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Creates all the tables defined in models module
create_db_and_tables()

# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Imagenet prediction endpoint
@app.post("/")
async def home_imagenet_predict(request: Request, file: UploadFile = File(...)):
    result = None
    error = None
    try:
        result = get_result(image_file=file)
    except Exception as ex:
        error = ex
    return templates.TemplateResponse("index.html", {"request": request, "result": result , "error": error})

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

@app.get("/download/toolwear-data")
async def download_toolwear_data(db: Session = Depends(get_db)):
    # Query all the records from the UpdateCNCMachine table
    records = db.query(UpdateCNCMachine).all()
    
    # Convert the records to a DataFrame
    df = pd.DataFrame([record.dict() for record in records])
    
    # Define the file path
    # file_path = "/home/train/datasets/current_machine_status_data.csv"
    
    # Save the DataFrame as a CSV file
    df.to_csv(dataset_save_path, index=False)
    
    # Return the CSV file as a download response
    return FileResponse(dataset_save_path, media_type='text/csv', filename=dataset_save_path)

@app.post("/load/train-data-to-db")
async def load_train_data_to_db():
    insert_train_data_to_db()
    return {"message": "Train data loaded successfully!"}
