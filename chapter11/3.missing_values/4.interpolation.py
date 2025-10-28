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

df['close_linear'] = df['close'].interpolate(method='linear')

df['close_poly'] = df['close'].interpolate(method='polynomial', order=3)

df['close_spline'] = df['close'].interpolate(method='spline', order=3)

print(df.head(30))

def plot_filled(ax, original, filled, label, color):
    ax.plot(filled, label=label, linestyle='-', color=color)
    filled_values = filled[original.isna()]
    ax.plot(filled_values.index, filled_values, 'o', color=color, markersize=5)
    ax.legend()

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(14, 18), sharex=True)


plot_filled(axes[0], df['close'], df['close_linear'], 'Linear Interpolation', 'purple')
axes[0].set_title('Linear Interpolation')

plot_filled(axes[1], df['close'], df['close_poly'], 'Polynomial Interpolation', 'orange')
axes[1].set_title('Polynomial Interpolation')

plot_filled(axes[2], df['close'], df['close_spline'], 'Spline Interpolation', 'brown')
axes[2].set_title('Spline Interpolation')

plt.xlabel('Date')
fig.supylabel('Stock Price (Close)')

plt.tight_layout()
plt.show()