import os
import joblib
from sklearn.preprocessing import StandardScaler

# Create models folder
os.makedirs("models", exist_ok=True)

def create_scaler(n_features, name):
    scaler = StandardScaler()
    dummy_data = [[0]*n_features, [1]*n_features]
    scaler.fit(dummy_data)
    joblib.dump(scaler, f"models/{name}_scaler.pkl")

# Create scalers
create_scaler(3, "blood")
create_scaler(3, "lft")
create_scaler(2, "kft")
create_scaler(2, "diabetes")
create_scaler(3, "lipid")
create_scaler(3, "thyroid")
create_scaler(3, "urine")
create_scaler(2, "bone")
create_scaler(2, "bp")
create_scaler(3, "sono")

print("✅ All scalers created successfully!")