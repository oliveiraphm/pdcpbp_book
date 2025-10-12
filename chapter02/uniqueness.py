import pandas as pd

data = {
   'Email': ['john.doe@example.com', 'jane.smith@example.com', 'james.doe@example.com', 'susan.brown@example.com'], 
}

df = pd.DataFrame(data)

duplicated_mask = df['Email'].duplicated(keep='first')

df['Uniqueness'] = ~duplicated_mask

unique_percentage = (df['Uniqueness'].sum() / len(df)) * 100

print("Dataset with Uniqueness Check:")
print(df)

print(f"Percentage of Unique Records: {unique_percentage:.2f}%")