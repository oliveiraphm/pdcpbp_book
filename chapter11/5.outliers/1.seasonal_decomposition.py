import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
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

result = seasonal_decompose(df['close'], model='additive', period=252, extrapolate_trend='freq')

df['trend'] = result.trend
df['seasonal'] = result.seasonal
df['residual'] = result.resid

df['resid_z'] = zscore(df['residual'].dropna())

outliers = df[np.abs(df['resid_z']) > 3]

median_resid = df['residual'].median()
df.loc[outliers.index, 'close'] = df['close'].median()

print(df[['close', 'close', 'trend', 'seasonal', 'residual', 'resid_z']].head(20))

fig, axes = plt.subplots(4, 1, figsize=(14, 18), sharex=True)

result.observed.plot(ax=axes[0], title='Observed', color='blue')
result.trend.plot(ax=axes[1], title='Trend', color='orange')
result.seasonal.plot(ax=axes[2], title='Seasonal', color='green')
result.resid.plot(ax=axes[3], title='Residual', color='red')

plt.tight_layout()
plt.show()