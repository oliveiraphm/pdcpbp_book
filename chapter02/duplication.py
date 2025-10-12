import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 101, 104, 105, 102],
    'FirstName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Bob'],
    'LastName': ['Smith', 'Johnson', 'Brown', 'Davis', 'Lee', 'White', 'Johnson'],
}

df = pd.DataFrame(data)

duplicated_mask = df.duplicated(subset='EmployeeID', keep='first')

df['IsDuplicate'] = duplicated_mask

duplicate_percentage = (df['IsDuplicate'].sum() / len(df)) * 100

print("Dataset with Duplicate Records:")
print(df)

print(f"Percentage of Duplicate Records: {duplicate_percentage:.2f}%")