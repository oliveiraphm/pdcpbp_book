import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from scipy.stats import zscore

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


outlier_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[outlier_indices[:5], 'close'] = df['close'] * 1.5
df.loc[outlier_indices[5:], 'close'] = df['close'] * 0.5

model = ARIMA(df['close'], order=(2, 1, 1))
results = model.fit()

df['residuals'] = results.resid
df['residuals_z'] = zscore(df['residuals'].dropna())

outliers_arima = df[np.abs(df['residuals_z']) > 3]
df['arima_smooth'] = results.fittedvalues

plt.figure(figsize=(14, 8))
plt.plot(df['close'], label='Original Close', color='blue')
plt.plot(df['arima_smooth'], label='ARIMA Smoothed', color='red')
plt.scatter(outliers_arima.index, df.loc[outliers_arima.index, 'close'], color='orange', label='Outliers')
plt.title('ARIMA Smoothing and Outlier Detection')
plt.legend()
plt.show()

print(results.summary())

results.plot_diagnostics(figsize=(14, 8))
plt.show()