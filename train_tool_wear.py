import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import *

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

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


print(df.head())

y = df["TARGET"]
X = df.drop(["TARGET"], axis=1)

# Split the data into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

