def load_data():
"""
Load a predefined electric car dataset.

Returns:
    pd.DataFrame: Loaded dataset as a Pandas DataFrame.
"""
data = """Make,Model,Year,BatteryCapacity_kWh,Range_km,Price
Tesla,Model 3,2021,75,450,50000
Nissan,Leaf,2019,40,240,30000
Chevrolet,Bolt EV,2020,66,380,37000
Hyundai,Kona Electric,2021,64,415,40000
Volkswagen,ID.4,2022,77,520,45000
BMW,i3,2018,33,200,29000
"""
return pd.read_csv(pd.compat.StringIO(data))

def preprocess_data(data):
"""
Preprocess the electric car dataset by handling missing values and encoding categorical variables.
"""
data = data.dropna()
data = pd.get_dummies(data, columns=['Make', 'Model'], drop_first=True)
return data

def analyze_data(data):
"""
Perform exploratory data analysis on the dataset.
"""
print("Dataset Summary:")
print(data.describe())

sns.pairplot(data[['Year', 'BatteryCapacity_kWh', 'Range_km', 'Price']])
plt.show()
def train_model(data):
"""
Train a predictive model using the dataset.

Returns:
    tuple: Trained model, test features, test labels, scaler
"""
features = data.drop(columns=['Price'])
target = data['Price']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

return model, X_test, y_test, scaler
def evaluate_model(model, X_test, y_test):
"""
Evaluate the trained model using Mean Squared Error and R-squared metrics.
"""
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
def visualize_results(model, X_test, y_test):
"""
Visualize the actual vs predicted prices and feature importance.
"""
y_pred = model.predict(X_test)

# Actual vs Predicted Prices
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Prices')
plt.show()

# Feature Coefficients
coefficients = model.coef_
feature_names = list(X_test.columns)
plt.figure(figsize=(8, 4))
plt.bar(feature_names, coefficients, color='skyblue')
plt.title('Feature Coefficients')
plt.xticks(rotation=45)
plt.ylabel('Coefficient Value')
plt.show()
def save_model(model, scaler, filename="electric_car_price_model.pkl"):
"""
Save the trained model and scaler to a file.
"""
joblib.dump({'model': model, 'scaler': scaler}, filename)
print(f"Model saved as {filename}")

if name == "main":
data = load_data()
data = preprocess_data(data)
analyze_data(data)
model, X_test, y_test, scaler = train_model(data)
evaluate_model(model, X_test, y_test)
visualize_results(model, X_test, y_test)
save_model(model, scaler)