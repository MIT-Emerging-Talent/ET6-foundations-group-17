import pandas as pd
from electric_car_prices_analysis import (
    load_data,
    preprocess_data,
    train_model,
    evaluate_model,
    save_model,
)

def test_load_data():
    """
    Test the load_data function to ensure it returns a DataFrame with correct columns.
    """
    data = load_data()
    assert isinstance(data, pd.DataFrame), "load_data() should return a DataFrame"
    expected_columns = ["Make", "Model", "Year", "BatteryCapacity_kWh", "Range_km", "Price"]
    assert list(data.columns) == expected_columns, f"Expected columns: {expected_columns}, but got {list(data.columns)}"
    print("test_load_data passed!")

def test_preprocess_data():
    """
    Test the preprocess_data function to ensure it cleans the data and encodes categorical variables.
    """
    data = load_data()
    processed_data = preprocess_data(data)
    assert not processed_data.isnull().any().any(), "preprocess_data() should remove missing values"
    assert "Make_Tesla" in processed_data.columns, "preprocess_data() should encode categorical variables"
    print("test_preprocess_data passed!")

def test_train_model():
    """
    Test the train_model function to ensure the model trains correctly and splits the data properly.
    """
    data = load_data()
    processed_data = preprocess_data(data)
    model, X_test, y_test, scaler = train_model(processed_data)
    assert hasattr(model, "predict"), "train_model() should return a trained model"
    assert len(X_test) > 0, "X_test should not be empty"
    assert len(y_test) > 0, "y_test should not be empty"
    print("test_train_model passed!")

def test_evaluate_model():
    """
    Test the evaluate_model function to ensure it calculates metrics without errors.
    """
    data = load_data()
    processed_data = preprocess_data(data)
    model, X_test, y_test, _ = train_model(processed_data)
    try:
        evaluate_model(model, X_test, y_test)
        print("test_evaluate_model passed!")
    except Exception as e:
        assert False, f"evaluate_model() raised an exception: {e}"

def test_save_model():
    """
    Test the save_model function to ensure the model is saved correctly.
    """
    data = load_data()
    processed_data = preprocess_data(data)
    model, _, _, scaler = train_model(processed_data)
    save_model(model, scaler, "test_model.pkl")
    try:
        import joblib
        saved_data = joblib.load("test_model.pkl")
        assert "model" in saved_data and "scaler" in saved_data, "save_model() should save both the model and scaler"
        print("test_save_model passed!")
    except Exception as e:
        assert False, f"save_model() failed to save or load the model: {e}"

if _name_ == "_main_":
    test_load_data()
    test_preprocess_data()
    test_train_model()
    test_evaluate_model()
    test_save_model()
    print("All tests passed!")
