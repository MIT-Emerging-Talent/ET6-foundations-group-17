# housing_prices_analysis_solution.py

def load_data():
    """
    Load a predefined housing dataset.

    Returns:
        pd.DataFrame: Loaded dataset as a Pandas DataFrame.
    """
    import pandas as pd
    from io import StringIO

    # Embedded dataset
    data = """SquareFeet,Bedrooms,Bathrooms,YearBuilt,LocationScore,Price
1500,3,2,2000,85,300000
2000,4,3,2010,90,450000
1800,3,2,2005,88,350000
2400,4,3,2020,92,500000
1600,3,2,1995,80,280000
1200,2,1,1980,70,200000
"""
    return pd.read_csv(StringIO(data))

def preprocess_data(data):
    """
    Preprocess the housing dataset by handling missing values and extracting necessary features.
    """
    return data.dropna()

def analyze_data(data):
    """
    Perform exploratory data analysis on the dataset.
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    print("Dataset Summary:")
    print(data.describe())

    sns.pairplot(data[['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'LocationScore', 'Price']])
    plt.show()

def train_model(data):
    """
    Train a predictive model using the dataset.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression

    features = ['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt', 'LocationScore']
    target = 'Price'

    X = data[features]
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using Mean Squared Error and R-squared metrics.
    """
    from sklearn.metrics import mean_squared_error, r2_score

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

def visualize_results(model, X_test, y_test):
    """
    Visualize the actual vs predicted prices and feature importance.
    """
    import matplotlib.pyplot as plt
    import pandas as pd

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
    coefficients = pd.Series(model.coef_, index=X_test.columns)
    plt.figure(figsize=(8, 4))
    coefficients.plot(kind='bar', color='skyblue')
    plt.title('Feature Coefficients')
    plt.ylabel('Coefficient Value')
    plt.show()

if _name_ == "_main_":
    data = load_data()
    data = preprocess_data(data)
    analyze_data(data)
    model, X_test, y_test = train_model(data)
    evaluate_model(model, X_test, y_test)
    visualize_results(model, X_test, y_test)