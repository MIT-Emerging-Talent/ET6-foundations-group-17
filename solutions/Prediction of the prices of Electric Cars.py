def load_data():
"""
Load a predefined electric car dataset.

Returns:
pd.DataFrame: loaded dataset as a Pandas DataFrame.
"""
import pandas as pd
from io import StringIO

try:
    # Embedded electric car dataset
    data = """Make,Model,Year,BatteryCapacity_kWh,Range_km,Price
Tesla,Model 3,2021,75,450,50000
Nissan,Leaf,2019,40,240,30000
Chevrolet,Bolt EV,2020,66,380,37000
Hyundai,Kona Electric,2021,64,415,40000
Volkswagen,ID.4,2022,77,520,45000
BMW,i3,2018,33,200,29000
"""
return pd.read_csv(StringIO(data))
except Exception as e:
print(f"Error loading data: {e}")
return pd.DataFrame()

def preprocess_data(data):
"""
Preprocess the electric car dataset by handling missing values and encoding categorical variables.
"""
import pandas as pd

try:
    data = data.dropna()
    # One-hot encode 'Make' and 'Model'
    data = pd.get_dummies(data, columns=['Make', 'Model'], drop_first=True)
    return data
except Exception as e:
    print(f"Error preprocessing data: {e}")
    return pd.DataFrame()
def analyze_data(data):
"""
Perform exploratory data analysis on the dataset.
"""
import matplotlib.pyplot as plt
import seaborn as sns

try:
    print("Dataset Summary:")
    print(data.describe())

    sns.pairplot(data[['Year', 'BatteryCapacity_kWh', 'Range_km', 'Price']])
    plt.show()
except Exception as e:
    print(f"Error in data analysis: {e}")
def train_model(data):
"""
Train a predictive model using the dataset.

Returns:
    tuple: Trained model, test features, test labels
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

try:
    features = data.drop(columns='Price')
    target = data['Price']

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test, scaler
except Exception as e:
    print(f"Error in model training: {e}")
    return None, None, None, None
def evaluate_model(model, X_test, y_test):
"""
Evaluate the trained model using Mean Squared Error and R-squared metrics.
"""
from sklearn.metrics import mean_squared_error, r2_score

try:
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
except Exception as e:
    print(f"Error in model evaluation: {e}")
def visualize_results(model, X_test, y_test):
"""
Visualize the actual vs predicted prices and feature importance.
"""
import matplotlib.pyplot as plt
import numpy as np

try:
    # Actual vs Predicted Prices
    y_pred = model.predict(X_test)
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.title('Actual vs Predicted Prices')
    plt.show()

    # Feature Coefficients
    coefficients = model.coef_
    feature_names = ['Year', 'BatteryCapacity_kWh', 'Range_km'] + list(X_test.columns[3:])
    plt.figure(figsize=(8, 4))
    plt.bar(feature_names, coefficients, color='skyblue')
    plt.title('Feature Coefficients')
    plt.xticks(rotation=45)
    plt.ylabel('Coefficient Value')
    plt.show()
except Exception as e:
    print(f"Error in visualization: {e}")
def save_model(model, scaler, filename="electric_car_price_model.pkl"):
"""
Save the trained model and scaler to a file.
"""
import joblib

try:
    joblib.dump({'model': model, 'scaler': scaler}, filename)
    print(f"Model saved as {filename}")
except Exception as e:
    print(f"Error saving model: {e}")
if name == "main":
data = load_data()
if not data.empty:
data = preprocess_data(data)
analyze_data(data)
model, X_test, y_test, scaler = train_model(data)
if model:
evaluate_model(model, X_test, y_test)
visualize_results(model, X_test, y_test)
save_model(model, scaler)
