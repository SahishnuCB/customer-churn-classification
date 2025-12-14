from sklearn.linear_model import LogisticRegression

def baseline_model(X_train, X_test, y_train, y_test):
    print("\nBaseline Model Template Running...")

    # Minimal baseline (not tuned, not final)
    model = LogisticRegression(max_iter=100)
    try:
        model.fit(X_train, y_train)
        print("Training complete (template level).")
    except:
        print("Model could not train — preprocessing incomplete (expected).")

    print("Evaluation templates would go here.")
