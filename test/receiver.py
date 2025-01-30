import socket
import requests
import json

# API details
# API_URL = 'http://localhost:8003/predict/toolwear' # Only predict inputs
API_URL = 'http://localhost:8003/predict_and_insert/toolwear' # Predict and insert inputs

# Server setup
HOST = 'localhost'  # IP to listen on
PORT = 5         # Port to bind

# Function to send data to API
def send_to_api(data):
    response = requests.post(API_URL, json=data)
    return response.json()

# Start listening for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive data
            data = conn.recv(4096)  # Buffer size
            if not data:
                break
            
            # Decode and process
            received_data = json.loads(data.decode('utf-8'))
            # print("Received data:", received_data)
            
            # Send to API
            api_response = send_to_api(received_data)
            print("API Response:", api_response)
