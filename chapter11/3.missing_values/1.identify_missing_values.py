import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

date_range = pd.date_range(start='2020-01-01', end='2023-12-31', freq='B')

n = len(date_range)
data = {
    'open': np.random.uniform(100, 200, n),
    'high': np.random.uniform(200, 300, n),
    'low': np.random.uniform(50, 100, n),
    'close': np.random.uniform(100, 200, n)
}

df = pd.DataFrame(data, index=date_range)

nan_indices = np.random.choice(df.index, size=100, replace=False)
df.loc[nan_indices] = np.nan

missing_dates = np.random.choice(df.index, size=50, replace=False)
df = df.drop(missing_dates)

print("Initial DataFrame with Missing Values and Timestamps:\n", df.head())

missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

complete_index = pd.date_range(start=df.index.min(), end=df.index.max(), freq='B')
df_reindexed = df.reindex(complete_index)
missing_timestamps = df_reindexed[df_reindexed.isnull().all(axis=1)]

total_timestamps = len(complete_index)
missing_timestamps_count = missing_timestamps.shape[0]
missing_timestamps_percentage = (missing_timestamps_count / total_timestamps) * 100

print("\nMissing Timestamps:\n", missing_timestamps)
print(f"\nPercentage of Missing Timestamps: {missing_timestamps_percentage:.2f}%")

plt.figure(figsize=(14,7))
plt.plot(df.index, df['close'], marker='o', linestyle='-', label='Closing Price', color='blue')

for date in missing_dates:
    plt.axvline(x=date, color='red', linestyle='--', linewidth=1)

nan_dates = df.index[df['close'].isnull()]
plt.scatter(nan_dates, [df['close'].mean()] * len(nan_dates), color='orange', label ='NaN Values in Close', zorder=5)

plt.title('Daily Closing Prices with Missing Timestamps and NaN Values Highlighted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

print("\nNaN values were introduced randomly in the dataset and are highlighted in orange on the plot.\n"
      "Red dashed lines indicate missing timestamps where no data is available for the dates in the index.\n"
      "Blue line shows the closing prices with missing values removed.")