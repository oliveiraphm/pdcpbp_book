import pandas as pd

employee_data_1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']
})

employee_data_2 = pd.DataFrame({
    'employee_id': [6, 7, 8, 9, 10],
    'name': ['Frank', 'Grace', 'Hannah', 'Ian', 'Jill'],
    'department': ['Logistics', 'Marketing', 'IT', 'Marketing', 'Finance']
})

merged_data = pd.merge(employee_data_1, employee_data_2, on='employee_id', how='outer', suffixes=('_1', '_2'))

print("Merged Employee Data with Suffixes:")
print(merged_data)