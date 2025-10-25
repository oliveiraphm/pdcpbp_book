import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate student data with missing ages and test scores
data = {'Age': [18, 20, None, 22, 21, 19, None, 23, 18, 24, 40, 41, 45, None, 34, None, 25, 30, 32, 24, 35, 38, 76, 90],
        'Test_Score': [85, None, 90, 92, None, 88, 94, 91, None, 87, 75, 78, 80, None, 74, 20, 50, 68, None, 58, 48, 59, 10, 5]}

df = pd.DataFrame(data)


df.fillna(df.mean(), inplace=True)

print("Original Dtaaset Statistics:")
print(df.describe())

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' Before Outlier Handling")
plt.hist(df['Age'], bins=10, color='blue', alpha=0.7, label='Original')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' Before Outlier Handling")
plt.hist(df['Test_Score'], bins=10, color='orange', alpha=0.7, label='Original')
plt.legend()

plt.tight_layout()
plt.show()

df_trimmed = df[(df['Age'] >= df['Age'].quantile(0.1)) & (df['Age'] <= df['Age'].quantile(0.9))]

df_trimmed_mean = df_trimmed.mean()

print("\nTrimmed Dataset Statistics:")
print(df_trimmed.describe())

print("\nTrimmed Mean:")
print(df_trimmed_mean)

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'Age' After Trimming")
plt.hist(df_trimmed['Age'], bins=10, color='blue', alpha=0.7, label='Trimmed')
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Distribution of 'Test_Score' After Trimming")
plt.hist(df_trimmed['Test_Score'], bins=10, color='orange', alpha=0.7, label='Trimmed')
plt.legend()

plt.tight_layout()
plt.show()