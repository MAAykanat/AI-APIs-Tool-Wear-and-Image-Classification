import numpy as np
import pandas as pd
from models import RequestCNCMachine, UpdateCNCMachine

import torchvision.transforms as transforms
from torchvision import models
from PIL import Image

import json
import io
import datetime
import base64

# model 
model = models.densenet121(pretrained=True)
model.eval()

# imagenet classes
imagenet_class_index = json.load(open('./static/imagenet_class_index.json'))


def predict_tool_wear(estimator, request):
    
    X1_ACTUALPOSITION=request["X1_ACTUALPOSITION"]
    X1_ACTUALVELOCITY=request["X1_ACTUALVELOCITY"]
    X1_ACTUALACCELERATION=request["X1_ACTUALACCELERATION"]
    X1_COMMANDPOSITION=request["X1_COMMANDPOSITION"]
    X1_COMMANDVELOCITY=request["X1_COMMANDVELOCITY"]
    X1_COMMANDACCELERATION=request["X1_COMMANDACCELERATION"]
    X1_CURRENTFEEDBACK=request["X1_CURRENTFEEDBACK"]
    X1_DCBUSVOLTAGE=request["X1_DCBUSVOLTAGE"]
    X1_OUTPUTCURRENT=request["X1_OUTPUTCURRENT"]
    X1_OUTPUTVOLTAGE=request["X1_OUTPUTVOLTAGE"]
    X1_OUTPUTPOWER=request["X1_OUTPUTPOWER"]
    Y1_ACTUALPOSITION=request["Y1_ACTUALPOSITION"]
    Y1_ACTUALVELOCITY=request["Y1_ACTUALVELOCITY"]
    Y1_ACTUALACCELERATION=request["Y1_ACTUALACCELERATION"]
    Y1_COMMANDPOSITION=request["Y1_COMMANDPOSITION"]
    Y1_COMMANDVELOCITY=request["Y1_COMMANDVELOCITY"]
    Y1_COMMANDACCELERATION=request["Y1_COMMANDACCELERATION"]
    Y1_CURRENTFEEDBACK=request["Y1_CURRENTFEEDBACK"]
    Y1_DCBUSVOLTAGE=request["Y1_DCBUSVOLTAGE"]
    Y1_OUTPUTCURRENT=request["Y1_OUTPUTCURRENT"]
    Y1_OUTPUTVOLTAGE=request["Y1_OUTPUTVOLTAGE"]
    Y1_OUTPUTPOWER=request["Y1_OUTPUTPOWER"]
    Z1_ACTUALPOSITION=request["Z1_ACTUALPOSITION"]
    Z1_ACTUALVELOCITY=request["Z1_ACTUALVELOCITY"]
    Z1_ACTUALACCELERATION=request["Z1_ACTUALACCELERATION"]
    Z1_COMMANDPOSITION=request["Z1_COMMANDPOSITION"]
    Z1_COMMANDVELOCITY=request["Z1_COMMANDVELOCITY"]
    Z1_COMMANDACCELERATION=request["Z1_COMMANDACCELERATION"]
    Z1_CURRENTFEEDBACK=request["Z1_CURRENTFEEDBACK"]
    Z1_DCBUSVOLTAGE=request["Z1_DCBUSVOLTAGE"]
    Z1_OUTPUTCURRENT=request["Z1_OUTPUTCURRENT"]
    Z1_OUTPUTVOLTAGE=request["Z1_OUTPUTVOLTAGE"]
    S1_ACTUALPOSITION=request["S1_ACTUALPOSITION"]
    S1_ACTUALVELOCITY=request["S1_ACTUALVELOCITY"]
    S1_ACTUALACCELERATION=request["S1_ACTUALACCELERATION"]
    S1_COMMANDPOSITION=request["S1_COMMANDPOSITION"]
    S1_COMMANDVELOCITY=request["S1_COMMANDVELOCITY"]
    S1_COMMANDACCELERATION=request["S1_COMMANDACCELERATION"]
    S1_CURRENTFEEDBACK=request["S1_CURRENTFEEDBACK"]
    S1_DCBUSVOLTAGE=request["S1_DCBUSVOLTAGE"]
    S1_OUTPUTCURRENT=request["S1_OUTPUTCURRENT"]
    S1_OUTPUTVOLTAGE=request["S1_OUTPUTVOLTAGE"]
    S1_OUTPUTPOWER=request["S1_OUTPUTPOWER"]
    S1_SYSTEMINERTIA=request["S1_SYSTEMINERTIA"]
    M1_CURRENT_PROGRAM_NUMBER=request["M1_CURRENT_PROGRAM_NUMBER"]
    M1_SEQUENCE_NUMBER=request["M1_SEQUENCE_NUMBER"]
    M1_CURRENT_FEEDRATE=request["M1_CURRENT_FEEDRATE"]

    machine_status = [[X1_ACTUALPOSITION, X1_ACTUALVELOCITY, X1_ACTUALACCELERATION,
                       X1_COMMANDPOSITION, X1_COMMANDVELOCITY, X1_COMMANDACCELERATION,
                       X1_CURRENTFEEDBACK, X1_DCBUSVOLTAGE, X1_OUTPUTCURRENT,
                       X1_OUTPUTVOLTAGE, X1_OUTPUTPOWER, Y1_ACTUALPOSITION,
                       Y1_ACTUALVELOCITY, Y1_ACTUALACCELERATION, Y1_COMMANDPOSITION,
                       Y1_COMMANDVELOCITY, Y1_COMMANDACCELERATION, Y1_CURRENTFEEDBACK,
                       Y1_DCBUSVOLTAGE, Y1_OUTPUTCURRENT, Y1_OUTPUTVOLTAGE,
                       Y1_OUTPUTPOWER, Z1_ACTUALPOSITION, Z1_ACTUALVELOCITY,
                       Z1_ACTUALACCELERATION, Z1_COMMANDPOSITION, Z1_COMMANDVELOCITY,
                       Z1_COMMANDACCELERATION, Z1_CURRENTFEEDBACK, Z1_DCBUSVOLTAGE,
                       Z1_OUTPUTCURRENT, Z1_OUTPUTVOLTAGE, S1_ACTUALPOSITION,
                       S1_ACTUALVELOCITY, S1_ACTUALACCELERATION, S1_COMMANDPOSITION,
                       S1_COMMANDVELOCITY, S1_COMMANDACCELERATION, S1_CURRENTFEEDBACK,
                       S1_DCBUSVOLTAGE, S1_OUTPUTCURRENT, S1_OUTPUTVOLTAGE,
                       S1_OUTPUTPOWER, S1_SYSTEMINERTIA, M1_CURRENT_PROGRAM_NUMBER,
                       M1_SEQUENCE_NUMBER, M1_CURRENT_FEEDRATE]]


    machine_status_array = np.array(machine_status)
    print(machine_status_array)
    print("Machine status shape:", machine_status_array.shape)
    prediction = estimator.predict(machine_status_array)

    return prediction[0] 

def insert_machine_status(request, prediction, client_ip, db):
    new_machine_status = UpdateCNCMachine(
        X1_ACTUALPOSITION=request["X1_ACTUALPOSITION"],
        X1_ACTUALVELOCITY=request["X1_ACTUALVELOCITY"],
        X1_ACTUALACCELERATION=request["X1_ACTUALACCELERATION"],
        X1_COMMANDPOSITION=request["X1_COMMANDPOSITION"],
        X1_COMMANDVELOCITY=request["X1_COMMANDVELOCITY"],
        X1_COMMANDACCELERATION=request["X1_COMMANDACCELERATION"],
        X1_CURRENTFEEDBACK=request["X1_CURRENTFEEDBACK"],
        X1_DCBUSVOLTAGE=request["X1_DCBUSVOLTAGE"],
        X1_OUTPUTCURRENT=request["X1_OUTPUTCURRENT"],
        X1_OUTPUTVOLTAGE=request["X1_OUTPUTVOLTAGE"],
        X1_OUTPUTPOWER=request["X1_OUTPUTPOWER"],
        Y1_ACTUALPOSITION=request["Y1_ACTUALPOSITION"],
        Y1_ACTUALVELOCITY=request["Y1_ACTUALVELOCITY"],
        Y1_ACTUALACCELERATION=request["Y1_ACTUALACCELERATION"],
        Y1_COMMANDPOSITION=request["Y1_COMMANDPOSITION"],
        Y1_COMMANDVELOCITY=request["Y1_COMMANDVELOCITY"],
        Y1_COMMANDACCELERATION=request["Y1_COMMANDACCELERATION"],
        Y1_CURRENTFEEDBACK=request["Y1_CURRENTFEEDBACK"],
        Y1_DCBUSVOLTAGE=request["Y1_DCBUSVOLTAGE"],
        Y1_OUTPUTCURRENT=request["Y1_OUTPUTCURRENT"],
        Y1_OUTPUTVOLTAGE=request["Y1_OUTPUTVOLTAGE"],
        Y1_OUTPUTPOWER=request["Y1_OUTPUTPOWER"],
        Z1_ACTUALPOSITION=request["Z1_ACTUALPOSITION"],
        Z1_ACTUALVELOCITY=request["Z1_ACTUALVELOCITY"],
        Z1_ACTUALACCELERATION=request["Z1_ACTUALACCELERATION"],
        Z1_COMMANDPOSITION=request["Z1_COMMANDPOSITION"],
        Z1_COMMANDVELOCITY=request["Z1_COMMANDVELOCITY"],
        Z1_COMMANDACCELERATION=request["Z1_COMMANDACCELERATION"],
        Z1_CURRENTFEEDBACK=request["Z1_CURRENTFEEDBACK"],
        Z1_DCBUSVOLTAGE=request["Z1_DCBUSVOLTAGE"],
        Z1_OUTPUTCURRENT=request["Z1_OUTPUTCURRENT"],
        Z1_OUTPUTVOLTAGE=request["Z1_OUTPUTVOLTAGE"],
        S1_ACTUALPOSITION=request["S1_ACTUALPOSITION"],
        S1_ACTUALVELOCITY=request["S1_ACTUALVELOCITY"],
        S1_ACTUALACCELERATION=request["S1_ACTUALACCELERATION"],
        S1_COMMANDPOSITION=request["S1_COMMANDPOSITION"],
        S1_COMMANDVELOCITY=request["S1_COMMANDVELOCITY"],
        S1_COMMANDACCELERATION=request["S1_COMMANDACCELERATION"],
        S1_CURRENTFEEDBACK=request["S1_CURRENTFEEDBACK"],
        S1_DCBUSVOLTAGE=request["S1_DCBUSVOLTAGE"],
        S1_OUTPUTCURRENT=request["S1_OUTPUTCURRENT"],
        S1_OUTPUTVOLTAGE=request["S1_OUTPUTVOLTAGE"],
        S1_OUTPUTPOWER=request["S1_OUTPUTPOWER"],
        S1_SYSTEMINERTIA=request["S1_SYSTEMINERTIA"],
        M1_CURRENT_PROGRAM_NUMBER=request["M1_CURRENT_PROGRAM_NUMBER"],
        M1_SEQUENCE_NUMBER=request["M1_SEQUENCE_NUMBER"],
        M1_CURRENT_FEEDRATE=request["M1_CURRENT_FEEDRATE"],
        prediction=prediction,
        client_ip=client_ip
    )

    with db as session:
        session.add(new_machine_status)
        session.commit()
        session.refresh(new_machine_status)
    
    return new_machine_status

# Image recognation functions

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]


def get_result(image_file,is_api = False):
    start_time = datetime.datetime.now()
    image_bytes = image_file.file.read()
    class_id,class_name = get_prediction(image_bytes)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    encoded_string = base64.b64encode(image_bytes)
    bs64 = encoded_string.decode('utf-8')
    image_data = f'data:image/jpeg;base64,{bs64}'   
    result = {
        "inference_time":execution_time,
        "predictions":{
            "class_id":class_id,
            "class_name":class_name
        }
    }
    if not is_api: 
        result["image_data"]= image_data
    return result