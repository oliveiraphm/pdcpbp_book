import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(0)
n_samples = 100
start_time = datetime(2023, 10, 25, 9, 0, 0)
end_time = datetime(2023, 10, 25, 16, 0, 0)

timestamps = [start_time + timedelta(minutes=np.random.randint(0, (end_time - start_time).total_seconds() / 60)) for _ in range(n_samples)]
values = np.random.randint(50, 101, n_samples)

df = pd.DataFrame({'Timestamp': timestamps, 'Value': values})

reference_timestamp = datetime(2023, 10, 25, 12, 0, 0)

timeliness_threshold = 30

df['Timeliness'] = (reference_timestamp - df['Timestamp']).dt.total_seconds() / 60
df['Timely'] = df['Timeliness'] <= timeliness_threshold

average_timeliness = df['Timeliness'].mean()

print("Dataset with Timestamps:")
print(df.head())

print("\nAverage Timeliness (in minutes):", average_timeliness)
print("Percentage of Timely Records:", (df['Timely'].sum() / n_samples) * 100, "%")