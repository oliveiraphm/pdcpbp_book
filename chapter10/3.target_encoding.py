import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from category_encoders import TargetEncoder
from sklearn.ensemble import RandomForestRegressor

sns.set(style="whitegrid")

np.random.seed(42)

n_samples = 1000

data = {
    'Store Type': np.random.choice(['Type A', 'Type B', 'Type C', 'Type D'], size=n_samples),
    'Number of Employees': np.random.randint(5, 50, size=n_samples),
    'Advertising Budget': np.random.uniform(1000, 50000, size=n_samples),
    'Daily Sales': np.random.uniform(500, 20000, size=n_samples)
}

df = pd.DataFrame(data)

print("Column Explanations:")
print("1. Store Type: The type of store (categorical variable with values 'Type A', 'Type B', 'Type C', 'Type D').")
print("2. Number of Employees: The number of employees working at the store (integer variable).")
print("3. Advertising Budget: The budget allocated for advertising by the store (continuous variable in dollars).")
print("4. Daily Sales: The sales made by the store in a day (target variable in dollars).")

X = df.drop(columns=['Daily Sales'])
y = df['Daily Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

target_encoder = TargetEncoder(cols=['Store Type'])

X_train_encoded = target_encoder.fit_transform(X_train, y_train)

X_test_encoded = target_encoder.transform(X_test)

print("\nX_train (original):")
print(X_train.head())
print("\nX_train_encoded:")
print(X_train_encoded.head())

plt.figure(figsize=(14,6))

plt.subplot(1, 2, 1)
sns.countplot(data=X_train, x='Store Type', palette='viridis')
plt.title('Distribution of Store Type Before Encoding')
plt.xticks(rotation=45)

encoded_col_name = 'Store Type'
plt.subplot(1, 2, 2)
sns.histplot(X_train_encoded[encoded_col_name], kde=True, bins=10, color='blue')
plt.title('Distribution of Store Type After Encoding')
plt.xlabel('Encoded Value')

plt.tight_layout()
plt.show()

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_encoded, y_train)

y_pred = model.predict(X_test_encoded)

mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error: {mse:.2f}")

baseline_pred = [y_train.mean()] * len(y_test)
baseline_mse = mean_squared_error(y_test, baseline_pred)
print(f"Baseline Mean Squared Error: {baseline_mse:.2f}")

if mse > baseline_mse:
    print("\nThe model's MSE is higher than the baseline MSE, indicating the model is not performing well.")
    print("Consider the following improvements:")
    print("1. Feature Engineering: Create new features or transform existing ones.")
    print("2. Model Tuning: Experiment with different hyperparameters or algorithms.")
    print("3. Data Quality: Check for data quality issues like missing values or outliers.")
    print("4. Additional Data: Collect more data or use additional relevant features.")
else:
    print("\nThe model is performing better than the baseline.")

X['Employees to Budget Ratio'] = X['Number of Employees'] / X['Advertising Budget']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_encoded = target_encoder.fit_transform(X_train, y_train)
X_test_encoded = target_encoder.transform(X_test)
model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train_encoded, y_train)
y_pred = model.predict(X_test_encoded)
mse = mean_squared_error(y_test, y_pred)
print(f"\nMean Squared Error after improvements: {mse:.2f}")

