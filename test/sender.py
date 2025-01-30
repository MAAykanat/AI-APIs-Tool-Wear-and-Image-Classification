import socket
import json
import time
import pandas as pd
import random

# Server details
HOST = 'localhost'  # IP of the machine running Script 2
PORT = 5        # Port to connect to Script 2

# Load and preprocess the dataset
df = pd.read_csv("dataset/test.csv")
df.columns = df.columns.str.upper()
df["TARGET"] = df["TARGET"].apply(lambda x: 1 if x == "worn" else 0)  # Convert to binary
df.drop(["EXP_NO", "MACHINING_PROCESS", "TARGET"], axis=1, inplace=True)  # Drop unnecessary columns

# Establish a connection and send data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the receiver
    while True:
        # Select a random row from the dataframe
        random_number = random.randint(0, df.shape[0] - 1)
        data_to_send = df.iloc[random_number].to_dict()

        # Convert the dictionary to JSON and send
        s.sendall(json.dumps(data_to_send).encode('utf-8'))
        print("Data sent:", data_to_send)
        time.sleep(5)  # Wait 5 seconds before sending the next batch
