import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

_model = None
_load_error = None

_DATA_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases"
    "/concrete/compressive/Concrete_Data.xls"
)
_COLS = ["cement", "slag", "flyash", "water", "superplasticizer",
         "coarseagg", "fineagg", "age", "strength"]


def initialize():
    global _model, _load_error
    try:
        df = pd.read_excel(_DATA_URL)
        df.columns = _COLS
        X = df.drop("strength", axis=1)
        y = df["strength"]
        _model = RandomForestRegressor(n_estimators=100, random_state=42)
        _model.fit(X, y)
        _load_error = None
        print("[ML] Model training complete (1,030 samples, Random Forest)")
    except Exception as e:
        _load_error = str(e)
        _model = None
        print(f"[ML] Model load failed: {e}")


def predict(cement, slag, flyash, water, superplasticizer, coarseagg, fineagg, age=28):
    if _model is None:
        initialize()
    if _model is None:
        return None
    x = np.array([[cement, slag, flyash, water, superplasticizer, coarseagg, fineagg, age]])
    return round(float(_model.predict(x)[0]), 1)


def is_ready():
    return _model is not None


def get_error():
    return _load_error
