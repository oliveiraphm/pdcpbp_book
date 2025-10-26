import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

data.hist(figsize=(12, 10), bins=20, color='blue', alpha=0.7)
plt.suptitle('Original Data Distributions')
plt.show()


data_zscore = (data - data.mean()) / data.std()

print("\nDataset Statistics after Z-score Scaling:")
print(data_zscore.describe())

data_zscore.hist(figsize=(12, 10), bins=20, color='green', alpha=0.7)
plt.suptitle('Data Distributions after Z-score Scaling')
plt.show()