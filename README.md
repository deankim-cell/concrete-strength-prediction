# Concrete Compressive Strength — ML Prediction & Mix Design System

> Civil Engineering · Machine Learning · Flask Web Application  
> **University of Florida** | Dean Kim | 2025

---

## Project Overview

Concrete compressive strength testing traditionally requires **28 days of curing** and costly lab work.
This project started as a machine learning model to predict strength instantly from mix design parameters —
and evolved into a full **web application** that recommends mix designs, estimates cost, and predicts strength in real time.

---

## Phase 1 — ML Strength Predictor *(original work)*

**`streamlit_app.py`**

Built independently using Python and scikit-learn. Trained a Random Forest model on the UCI Concrete Dataset (Yeh, 1998) to predict 28-day compressive strength from mix ingredients.

| Model | R² Score |
|-------|----------|
| Linear Regression | 0.628 |
| **Random Forest** | **0.854** |

**Key findings:**
- Age > Cement > Water are the most influential features
- Non-linear relationships explain Linear Regression's limitations
- Results align with civil engineering theory (water-cement ratio effect)

**Tools:** Python · pandas · scikit-learn · matplotlib · Google Colab

---

## Phase 2 — Full Mix Design Web Application *(expanded with AI assistance)*

**`app.py` · `concrete_data.py` · `ml_model.py`**

Expanded the ML predictor into a complete engineering tool with:

- **Mix Design Recommender** — selects concrete grade (fck) based on building type, number of floors, use case (coastal, underground, bridge, etc.), and structural member, following ACI 318 / KDS 14 20 10 standards
- **ML Strength Prediction** — the original Random Forest model integrated into the web app, predicting 28-day strength for any recommended mix
- **Real-Time Cost Analysis** — calculates material cost per m³ with region-specific pricing (9 US regions including 4 Florida zones), user-editable prices
- **Material Guide** — role, application, and effect of each concrete ingredient

**Tools:** Python · Flask · pandas · scikit-learn · HTML/CSS · JavaScript

---

## Dataset

- **Source:** UCI Machine Learning Repository — Yeh, I-C. (1998)
- **Samples:** 1,030
- **Features:** Cement, Blast Furnace Slag, Fly Ash, Water, Superplasticizer, Coarse Aggregate, Fine Aggregate, Age (days)
- **Target:** Compressive Strength (MPa)

---

## Running Locally

```bash
pip install -r requirements.txt

# Flask web app (Phase 2)
python app.py

# Streamlit ML predictor (Phase 1)
streamlit run streamlit_app.py
```

---

## Why This Matters

Accurate strength prediction enables engineers to:
- Optimize mix designs without waiting 28 days per test
- Reduce laboratory testing costs
- Make faster decisions during the structural design phase
- Compare cost efficiency across regional material prices
