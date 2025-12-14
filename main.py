from eda import run_basic_eda
from preprocess import preprocess_data
from model import baseline_model

def main():
    print("=== PARTIAL CHURN PROJECT TEMPLATE ===")

    print("\n[1] Running basic EDA (partial)...")
    run_basic_eda()

    print("\n[2] Running preprocessing (template only)...")
    X_train, X_test, y_train, y_test = preprocess_data()

    print("\n[3] Running baseline model (not fully trained)...")
    baseline_model(X_train, X_test, y_train, y_test)

    print("\nTemplate complete (NOT a finished project).")

if __name__ == '__main__':
    main()
