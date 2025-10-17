import pandas as pd

employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'IT', 'Marketing', 'Finance', 'IT', 'IT']
})

project_data = pd.DataFrame({
    'employee_id': [2, 3, 4, 5, 5, 6],
    'project_name': ['ProjectA', 'ProjectB', 'ProjectC', 'ProjectD', 'ProjectD', 'ProjectE']
})

employee_data = employee_data.drop_duplicates(subset="employee_id", keep="first")
project_data = project_data.drop_duplicates(subset="employee_id", keep="first")

merged_data = pd.merge(employee_data, project_data, on="employee_id", how="inner")

print("Merged Data Result after handling duplicates:")
print(merged_data)