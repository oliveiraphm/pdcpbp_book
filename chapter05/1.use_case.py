import pandas as pd

employee_data = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department':['HR', 'IT', 'Marketing', 'Finance', 'IT']
})

project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectE']
})

print("employee_data Result:")
print(employee_data)

print("project_data Result:")
print(project_data)