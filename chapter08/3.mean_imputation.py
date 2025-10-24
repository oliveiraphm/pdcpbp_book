import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)
print(df)

print("Original Dataset Statistics:")
print(df.describe())

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Mean Imputation")
plt.hist(df['Age'].dropna(), bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' Before Mean Imputation")
plt.hist(df['Test_Score'].dropna(), bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

df_mean_imputed = df.copy()
df_mean_imputed['Age'].fillna(round(df['Age'].mean()), inplace=True)
df_mean_imputed['Test_Score'].fillna(df['Test_Score'].mean(), inplace=True)

print("\nDataset after Mean Imputation:")
print(df_mean_imputed)

print("\nDataset Statistics after Mean Imputation:")
print(df_mean_imputed.describe())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Mean Imputation")
plt.hist(df_mean_imputed['Age'], bins=10, color='blue', alpha=0.7, label='Imputed')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Mean Imputation")
plt.hist(df_mean_imputed['Test_Score'], bins=10, color='orange', alpha=0.7, label='Imputed')
plt.legend()

plt.tight_layout()
plt.show()