import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

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

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plot_acf(df['close'].dropna(), lags=40, ax=plt.gca())
plt.title('Autocorrelation Function (ACF)')

plt.subplot(1, 2, 2)
plot_pacf(df['close'].dropna(), lags=40, ax=plt.gca())
plt.title('Partial Autocorrelation Function (PACF)')

plt.tight_layout()
plt.show()