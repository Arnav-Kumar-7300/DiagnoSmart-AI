import joblib

# Dummy scaler (you can keep if already used)
from sklearn.preprocessing import StandardScaler
import numpy as np

scaler = StandardScaler()
scaler.fit(np.random.rand(10, 5))

joblib.dump(scaler, "models/scalers.pkl")

print("Scaler saved successfully!")