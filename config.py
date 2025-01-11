import joblib
import pandas as pd

df_train = pd.read_csv('dataset/train.csv')

estimator_toolwear = joblib.load('saved_models/toolwear_RandomForestClassifier.pkl')

dataset_save_path = '/home/train/project/dataset/current_machine_status_data.csv'