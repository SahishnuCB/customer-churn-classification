
# Customer Churn Prediction Project

This project implements a full binary classification pipeline to predict customer churn
using the provided **Customer-Churn.csv** dataset.

## Contents

- `customer_churn_binary_classification.ipynb` — main Google Colab / Kaggle-ready notebook
- `Customer-Churn.csv` — original dataset (as provided)
- `README.md` — this file

## How to Run (Colab / Kaggle)

1. Upload all files from this ZIP:
   - `customer_churn_binary_classification.ipynb`
   - `Customer-Churn.csv`

2. Open `customer_churn_binary_classification.ipynb` in Google Colab or Kaggle.

3. Make sure the line

   ```python
   data_path = "Customer-Churn.csv"
   ```

   correctly points to the CSV file (adjust the path if needed).

4. Run all cells from top to bottom.

The notebook includes:

- Exploratory Data Analysis (EDA)
- Data cleaning & preprocessing
- Baseline model (most frequent class)
- Logistic Regression model
- Tuned Random Forest model
- Evaluation metrics (accuracy, precision, recall, F1)
- Confusion matrices
- Feature importance and discussion of limitations
