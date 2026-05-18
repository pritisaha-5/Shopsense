# src/train_model.py
import pandas as pd
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/processed/rfm_data.csv")

df["Churn"] = df["Segment"].apply(lambda x: 1 if x in ["Lost", "At Risk"] else 0)

X = df[["Recency", "Frequency", "Monetary"]]
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "models/churn_model.pkl")

print("Model recreated successfully")