import pandas as pd
from datetime import datetime

data = {
    'Timestamp': ['2023-10-25 10:00:00', '2023-10-25 11:00:00', '2023-10-25 12:00:00'],
    'Value': [50, 55, 60]
}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

reference_timestamp = datetime(2023, 10, 25, 12, 30, 0)

timeliness_check = df['Timestamp'] <= reference_timestamp

print("Timeliness Check:")
print(timeliness_check)