import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)

df.fillna(df.mean(), inplace=True)

print("Original Dataset Statistics:")
print(df.describe())

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Outlier Handling")
plt.hist(df['Age'], bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_score' Before Outlier Handling")
plt.hist(df['Test_Score'], bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

Q1 = df['Test_Score'].quantile(0.25)
Q3 = df['Test_Score'].quantile(0.75)
IQR = Q3 - Q1

outlier_threshold = 1.5
lower_bound = Q1 - outlier_threshold * IQR
upper_bound = Q3 + outlier_threshold * IQR

df_no_outliers = df[(df['Test_Score'] >= lower_bound) & (df['Test_Score'] <= upper_bound)].copy()

print("\nDataset after Outlier Handling:")
print(df_no_outliers)

print("\nDataset Statistics after Outlier Handling:")
print(df_no_outliers.describe())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Outlier Handling")
plt.hist(df_no_outliers['Age'], bins=10, color='blue', alpha=0.7, label='Cleaned')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Outlier Handling")
plt.hist(df_no_outliers['Test_Score'], bins=10, color='orange', alpha=0.7, label='Cleaned')
plt.legend()

plt.tight_layout()
plt.show()