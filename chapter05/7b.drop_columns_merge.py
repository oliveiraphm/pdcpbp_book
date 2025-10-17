import pandas as pd

employee_data_1 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT']  # More reliable department information
})

employee_data_2 = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['Human Resources', 'Information Technology', 'Sales', 'Financial', 'Technical']  # Less reliable, drop this
})

employee_data_2.drop(columns=['department'], inplace=True)

merged_data = pd.merge(employee_data_1, employee_data_2, on=['employee_id', 'name'], how='inner')

print("Merged Employee Data with More Reliable Department Information:")
print(merged_data)