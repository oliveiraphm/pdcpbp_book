import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

np.random.seed(42)
num_samples = 100

square_footage = np.random.uniform(500, 5000, num_samples)
distance_to_school = np.random.uniform(0.1, 5, num_samples)
commute_distance = np.random.exponential(5, num_samples)
traffic_density = np.random.exponential(2, num_samples)

data = pd.DataFrame({
    'Square_Footage': square_footage,
    'Distance_to_School': distance_to_school,
    'Commute_Distance': commute_distance,
    'Traffic_Density': traffic_density
})

print("Original Dataset Statistics:")
print(data.describe())

plt.figure(figsize=(12, 8))

for i, column in enumerate(data.columns):
    plt.subplot(2, 2, i+1)
    plt.title(f"Distribution of '{column}' Before Scaling")
    plt.hist(data[column], bins=20, color='blue', alpha=0.7)
    plt.xlabel(column)

plt.tight_layout()
plt.show()

robust_scaler = RobustScaler()
data_scaled = robust_scaler.fit_transform(data)

data_scaled = pd.DataFrame(data_scaled, columns=data.columns)

print("\nDataset after Robust Scaling:")
print(data_scaled.describe())

plt.figure(figsize=(12, 8))

for i, col in enumerate(data_scaled.columns, 1):
    plt.subplot(2, 2, i)
    plt.title(f"Distribution of {col} After Robust Scaling")
    plt.hist(data_scaled[col], bins=20, color='orange', alpha=0.7)

plt.tight_layout()
plt.show()