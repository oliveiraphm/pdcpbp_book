import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


np.random.seed(42)
data = np.random.multivariate_normal(mean=[0, 0], cov=[[1, 0.5], [0.5, 1]], size=100)
outliers = np.random.multivariate_normal(mean=[8, 8], cov=[[1, 0], [0, 1]], size=10)
data_with_outliers = np.vstack([data, outliers])

df = pd.DataFrame(data_with_outliers, columns=['Feature1', 'Feature2'])

plt.scatter(df['Feature1'], df['Feature2'], color='blue', label='Inliers')
plt.scatter(outliers[:, 0], outliers[:, 1], color='red', marker='x', label='Outliers')
plt.title('Original Data with Outliers')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.legend()
plt.show()

scaler=StandardScaler()
data_scaled = scaler.fit_transform(df)
dbscan = DBSCAN(eps=0.4, min_samples=5)
df['Outlier'] = dbscan.fit_predict(data_scaled)

plt.scatter(df['Feature1'][df['Outlier'] == -1], df['Feature2'][df['Outlier'] == -1], color='red', marker='x', label='Outliers')
plt.scatter(df['Feature1'][df['Outlier'] != -1], df['Feature2'][df['Outlier'] != -1], color='blue', label='Inliers')
plt.title('Outlier Detection with DBSCAN')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.legend()
plt.show()