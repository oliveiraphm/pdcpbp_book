import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age' : [25, 30, None, 28, 22],
    'Gender' : ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City' : ['New York', 'Los Angeles', 'Chicago', None, 'San Francisco'] 
}

df = pd.DataFrame(data)

completeness = df.isnull().sum()

total_records = len(df)
completeness_percentage = (1 - completeness / total_records) * 100

print("Completeness Check:")
print(completeness)
print("\nCompleteness Percentage:")
print(completeness_percentage)