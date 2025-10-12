import pandas as pd

data = {
    'ProductID' : [1, 2, 3, 4, 5],
    'ProductName': ['PROD001', 'PROD002', 'Product003', 'PROD004', 'PROD005'],
}

df = pd.DataFrame(data)

expected_prefix = "PROD"

inconsistent_mask = ~df['ProductName'].str.startswith(expected_prefix)

df['Consistency'] = ~inconsistent_mask

consistent_percentage = (df['Consistency'].sum() / len(df)) * 100

print("Dataset with Consistency Check:")
print(df)

print(f"Percentage of Consistent Rows: {consistent_percentage:.2f}%")