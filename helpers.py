import numpy as np
import pandas as pd
from models import RequestCNCMachine, UpdateCNCMachine
from io import StringIO
import os

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

# Define the function to fetch data from SQL and generate a CSV using Pandas
def download_from_sql_with_pandas(db):
    # Example query to fetch data (modify as needed)
    query = "SELECT * FROM machine_status"
    
    # Use Pandas to fetch data from the database
    df = pd.read_sql(query, db.bind)  # db.bind provides the database connection

    # Define the dataset folder and file path
    dataset_folder = "dataset"
    file_name = "current_machine_status_dataset.csv"
    file_path = os.path.join(dataset_folder, file_name)

    # Ensure the dataset folder exists
    os.makedirs(dataset_folder, exist_ok=True)

    # Save the DataFrame to a CSV file in the dataset folder
    df.to_csv(file_path, index=False)

    return print("Data downloaded successfully to:", file_path)