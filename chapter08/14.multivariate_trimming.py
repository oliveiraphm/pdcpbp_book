import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2
from mpl_toolkits.mplot3d import Axes3D


np.random.seed(42)
data = np.random.multivariate_normal(mean=[0, 0], cov=[[1, 0.5], [0.5, 1]], size=100)

outliers = np.array([[8, 8], [9, 9]])
data = np.concatenate([data, outliers])

df = pd.DataFrame(data, columns=['X1', 'X2'])

def mahalanobis_distance(x, mean, inv_cov_matrix):

    centered_data = x - mean
    
    mahalanobis_dist = np.sqrt(np.dot(centered_data, np.dot(inv_cov_matrix, centered_data)))
    
    return mahalanobis_dist

df[['X1', 'X2']] = df[['X1', 'X2']].astype(float)

mean = np.mean(df[['X1', 'X2']], axis=0)

cov_matrix = np.cov(df[['X1', 'X2']], rowvar=False)

inv_cov_matrix = np.linalg.inv(cov_matrix)

df['Mahalanobis_Distance'] = df.apply(lambda row: mahalanobis_distance(row[['X1', 'X2']], mean, inv_cov_matrix), axis=1)

alpha = 0.1
chi2_threshold = chi2.ppf(1 - alpha, df=2)  # df is the degrees of freedom, which is the number of features

outliers = df[df['Mahalanobis_Distance'] > chi2_threshold]

df_no_outliers = df[df['Mahalanobis_Distance'] <= chi2_threshold]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'X1' Before Outiler Handling")
sns.histplot(df['X1'], bins=20, color='blue', kde=True)
plt.xlabel('X1')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.title("Distribution of 'X2' Before Outlier Handling")
sns.histplot(df['X2'], bins=20, color='orange', kde=True)
plt.xlabel('X2')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.title("Distribution of 'X1' After Outlier Handling")
sns.histplot(df_no_outliers['X1'], bins=20, color='blue', kde=True)
plt.xlabel('X1')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.title("Distribution of 'X2' After Outlier Handling")
sns.histplot(df_no_outliers['X2'], bins=20, color='orange', kde=True)
plt.xlabel('X2')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df_no_outliers['X1'], df_no_outliers['X2'], df_no_outliers['Mahalanobis_Distance'], color='blue', label='Data Points')

ax.scatter(outliers['X1'], outliers['X2'], outliers['Mahalanobis_Distance'], color='red', marker='x', label='Outliers')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Mahalanobis Distance')
ax.set_title('Outlier Detection using Mahalanobis Distance')

plt.legend()
plt.show()

print('\nOriginal Dataset Statistics:')
print(df.describe())

print("\nDataset Statistics after Removing Outliers:")
print(df_no_outliers.describe())