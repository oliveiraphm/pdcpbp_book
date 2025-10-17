import pandas as pd

employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'IT', 'Marketing', 'Finance', 'IT', 'IT'],
    'salary': [50000, 60000, 60000, 55000, 65000, 70000, 70000]  # Added salary for aggregation
})

project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 7, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectD', 'ProjectE']
})

aggregated_employee_data = employee_data.groupby('employee_id').agg({
    'name': 'first',
    'department': 'first',
    'salary' : 'sum'
}).reset_index()

merged_data = pd.merge(aggregated_employee_data, project_data, on='employee_id', how='inner')

print("Merged Data Result after aggregation:")
print(merged_data)