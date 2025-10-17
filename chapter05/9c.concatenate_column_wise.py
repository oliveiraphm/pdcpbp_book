import pandas as pd
import numpy as np

employee_data_1 = pd.DataFrame({
    'employee_id': np.arange(1, 6),
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']
})

employee_performance = pd.DataFrame({
    'employee_id': np.arange(1, 6),
    'performance_rating': [3, 4, 5, 3, 4]
})

concatenated_data = pd.concat([employee_data_1, employee_performance], axis=1)

print("Concatenated Employee Data (Column-wise):")
print(concatenated_data)