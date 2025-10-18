import pandas as pd

data = {
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Sub-Category': ['Mobile', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch', 'Printer'],
    'Sales': [1000, 1500, 800, 300, 400, 600],
    'Quantity': [50, 25, 40, 15, 20, 30],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

filtered_data = df[(df['Sales'] > 1000) & (df['Quantity'] < 30)]

print("Filtered Data based on Multiple Criteria:")
print(filtered_data)