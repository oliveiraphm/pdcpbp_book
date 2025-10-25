import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)

df.fillna(df.mean(), inplace=True)

print("Original Dataset Statistics:")
print(df.describe())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Transformation")
plt.hist(df['Age'], bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' Before Transformation")
plt.hist(df['Test_Score'], bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

df_log_transformed = df.copy()
df_log_transformed['Age'] = np.log1p(df_log_transformed['Age'])
df_log_transformed['Test_Score'] = np.log1p(df_log_transformed['Test_Score'])

print("\nDataset after Logarithmic Transformation:")
print(df_log_transformed.describe())

df_sqrt_transformed = df.copy()
df_sqrt_transformed['Age'] = np.sqrt(df_sqrt_transformed['Age'])
df_sqrt_transformed['Test_Score'] = np.sqrt(df_sqrt_transformed['Test_Score'])

print("\nDataset after Square Root Transformation:")
print(df_sqrt_transformed.describe())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Transformation")
plt.hist(df_log_transformed['Age'], bins=10, color='blue', alpha=0.7, label='Log-Transformed')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Transformation")
plt.hist(df_log_transformed['Test_Score'], bins=10, color='orange', alpha=0.7, label='Log-Transformed')
plt.legend()

plt.tight_layout()
plt.show()