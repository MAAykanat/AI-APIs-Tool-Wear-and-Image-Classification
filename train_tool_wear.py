import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import *
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier

# Load the data
df = pd.read_csv('dataset/train.csv')

# Capitalize the column names
df.columns = df.columns.str.upper()

# Display the first 5 rows of the data
print(df.head())

df["TARGET"] = df["TARGET"].apply(lambda x: 1 if x == "worn" else 0) # Convert to binary

df.drop(["EXP_NO","MACHINING_PROCESS"], axis=1, inplace=True) # Drop the experiment number amd machining status column

# Shuffle dataset 
df = df.sample(frac=1).reset_index(drop=True)

print(df.head())


print(df.iloc[0])

y = df["TARGET"]
X = df.drop(["TARGET"], axis=1)

# Split the data into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([('scaler', StandardScaler()), ('classifier', RandomForestClassifier(n_estimators=500))])

# Fit Pipeline
pipeline.fit(X_train, y_train)

# Model Evaluation
y_pred = pipeline.predict(X_test)
print(f"Test Accuracy: {pipeline.score(X_test, y_test)}")


# Predict
df_test = df.drop(["TARGET"], axis=1)

single_input = df_test.iloc[0].to_numpy().reshape(1, -1)
# single_input = np.array([159.0, 0.825, 50.0, 159.0, 0.615).reshape(1, -1)
print('Input:', single_input)
print('Prediction:', pipeline.predict(single_input))

# Save the model
joblib.dump(pipeline, 'saved_models/toolwear_RandomForestClassifier.pkl')
