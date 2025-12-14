import pandas as pd

def run_basic_eda():
    df = pd.read_csv('Customer-Churn.csv')

    print("\n=== BASIC EDA ===")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)

    print("\nChurn Distribution:")
    print(df['Churn'].value_counts())

    print("\n(Plot templates would go here — not implemented)")
