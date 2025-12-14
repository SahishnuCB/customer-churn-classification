import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    df = pd.read_csv('Customer-Churn.csv')

    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    X = df.select_dtypes(include=['int64', 'float64'])
    y = df['Churn']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
