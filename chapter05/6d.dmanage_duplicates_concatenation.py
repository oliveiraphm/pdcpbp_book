import pandas as pd


employee_data = pd.DataFrame({
    'employee_id': [1, 2, 2, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eva', 'Eva'],
    'department': ['HR', 'IT', 'Marketing', 'Marketing', 'Finance', 'IT', 'HR']
})

print("Original Employee Data:")
print(employee_data)

employee_data['department'] = employee_data.groupby('employee_id')['department'].transform(lambda x: ', '.join(x))
employee_data = employee_data.drop_duplicates('employee_id')

print("\nModified Employee Data after Concatenation and Removing Duplicates:")
print(employee_data)