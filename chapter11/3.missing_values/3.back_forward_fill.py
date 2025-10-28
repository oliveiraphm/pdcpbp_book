import pandas as pd
import numpy as np

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

df['close_ffill'] = df['close'].ffill()
df['close_bfill'] = df['close'].bfill()

print("Complete DataFrame with Original and Filled Values:\n")
print(df[['open', 'close', 'close_ffill', 'close_bfill']].head(20)) 