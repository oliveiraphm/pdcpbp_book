import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age' : [25, 30, None, 28, 22],
    'Gender' : ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City' : ['New York', 'Los Angeles', 'Chicago', None, 'San Francisco'] 
}

reference_data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age' : [25, 30, 29, 28, 22],
    'Gender' : ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City' : ['New York', 'Los Angeles', 'Chicago', 'New York', 'San Francisco'] 
}

df = pd.DataFrame(data)
reference_df = pd.DataFrame(reference_data)

accuracy_check = df == reference_df

accuracy_percentage = accuracy_check.mean() * 100

print("Accuracy Check:")
print(accuracy_check)
print("\nAccuracy Percentage:")
print(accuracy_percentage)