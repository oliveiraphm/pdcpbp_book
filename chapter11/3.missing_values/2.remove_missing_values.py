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

nan_indices_close = np.random.choice(df.index, size=50, replace=False)
nan_indices_open = np.random.choice(df.index, size=50, replace=False)
df.loc[nan_indices_close, 'close'] = np.nan
df.loc[nan_indices_open, 'open'] = np.nan

print("Initial DataFrame with Missing Values:\n", df.head())


missing_values = df.isnull().sum()
print("\nMissing Values in Each Column:\n", missing_values)

missing_percentage = (missing_values / len(df)) * 100
print("\nPercentage of Missing Values in Each Column:\n", missing_percentage)

print(f"\nNumber of rows before dropping NaN values: {len(df)}")

df_cleaned = df.dropna()

print(f"\nNumber of rows after dropping NaN values: {len(df_cleaned)}")

cleaned_missing_values = df_cleaned.isnull().sum()
cleaned_missing_percentage = (cleaned_missing_values / len(df_cleaned)) * 100
print("\nPercentage of Missing Values After Dropping Rows:\n", cleaned_missing_percentage)

plt.figure(figsize=(14, 7))
plt.plot(df.index, df['close'], marker='o', linestyle='-', label='Original Closing Price', color='blue', alpha=0.5)

nan_dates_close = df.index[df['close'].isnull()]
nan_dates_open = df.index[df['open'].isnull()]

plt.title('Original Daily Closing Prices with NaN Values Highlighted')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Plotting cleaned data after dropping rows with NaN values
plt.figure(figsize=(14, 7))
plt.plot(df_cleaned.index, df_cleaned['close'], marker='o', linestyle='-', label='Cleaned Closing Price', color='green')

plt.title('Cleaned Daily Closing Prices After Dropping NaN Values')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()