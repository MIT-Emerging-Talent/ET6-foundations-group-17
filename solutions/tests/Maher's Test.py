import unittest
import pandas as pd
from io import StringIO
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Assuming the module is named housing_analysis and the functions are imported
from housing_analysis import (
    load_data, preprocess_data, analyze_data, train_model, evaluate_model, visualize_results
)

class TestHousingAnalysis(unittest.TestCase):
    
    def setUp(self):
        """Set up the dataset for testing."""
        self.data = load_data()
        
    def test_load_data(self):
        """Test if the data loads correctly."""
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertEqual(self.data.shape[0], 6)  # Should have 6 rows
        self.assertEqual(self.data.shape[1], 6)  # Should have 6 columns
        
        # Verify column names
        expected_columns = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'LocationScore', 'Price']
        self.assertListEqual(list(self.data.columns), expected_columns)

    def test_preprocess_data(self):
        """Test if preprocessing removes missing values."""
        processed_data = preprocess_data(self.data)
        self.assertFalse(processed_data.isnull().values.any())
        self.assertEqual(processed_data.shape, self.data.shape)  # No missing values in the initial dataset

    def test_analyze_data(self):
        """Test if analysis does not throw errors."""
        try:
            analyze_data(self.data)
        except Exception as e:
            self.fail(f"Analyze data failed with error: {e}")

    def test_train_model(self):
        """Test if the model trains correctly."""
        processed_data = preprocess_data(self.data)
        model, X_test, y_test = train_model(processed_data)
        
        self.assertIsInstance(model, LinearRegression)
        self.assertGreater(len(X_test), 0)  # Ensure test set is not empty
        self.assertGreater(len(y_test), 0)

        # Check that the model coefficients are not all zeros
        self.assertTrue(any(model.coef_ != 0), "Model coefficients should not all be zero.")

    def test_evaluate_model(self):
        """Test if model evaluation metrics are reasonable."""
        processed_data = preprocess_data(self.data)
        model, X_test, y_test = train_model(processed_data)
        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        self.assertGreaterEqual(mse, 0, "Mean Squared Error should be non-negative.")
        self.assertGreaterEqual(r2, -1, "R-squared should be greater than or equal to -1.")
        self.assertLessEqual(r2, 1, "R-squared should be less than or equal to 1.")

    def test_visualize_results(self):
        """Test if visualization functions run without errors."""
        processed_data = preprocess_data(self.data)
        model, X_test, y_test = train_model(processed_data)
        
        try:
            visualize_results(model, X_test, y_test)
        except Exception as e:
            self.fail(f"Visualization failed with error: {e}")

    def test_full_pipeline(self):
        """Test the full pipeline from data loading to visualization."""
        try:
            data = load_data()
            processed_data = preprocess_data(data)
            analyze_data(processed_data)
            model, X_test, y_test = train_model(processed_data)
            evaluate_model(model, X_test, y_test)
            visualize_results(model, X_test, y_test)
        except Exception as e:
            self.fail(f"Full pipeline failed with error: {e}")

if _name_ == "_main_":
    unittest.main()