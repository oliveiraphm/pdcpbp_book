import pandas as pd

data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'NewProductName': ['Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_A', 'Product_B', 'Product_C', 'Product_A', 'Product_B', 'Product_C'],
    'NewPurchaseAmount': [50, 75, 120, 60, 80, 55, 90, 110, 70, 85, 130],
    'PaymentMethod': ['Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card', 'PayPal', 'Cash', 'Card', 'Bank Transfer', 'Card'],
    'Timestamp': ['2022-01-01 08:30:45', '2022-01-02 14:20:30', '2022-01-03 20:15:10', '2022-01-04 12:45:30', '2022-01-05 18:10:55', '2022-01-06 09:30:15', '2022-01-07 15:40:20', '2022-01-08 22:25:50', '2022-01-09 14:55:45', '2022-01-10 19:30:10', '2022-01-11 08:45:30']
}

df = pd.DataFrame(data)

print("Initial E-commerce Dataset:")
print(df)

print("Initial Memory Usage:")
print(df.memory_usage().sum() / (1024 ** 2), "MB")

df_before_drop = df.copy()

columns_to_drop = ['CustomerID', 'Timestamp']

try:
    df.drop(columns=columns_to_drop, inplace=True)
except KeyError as ke:
    print(f"Error: {ke}")

print("\nDataFrame after Dropping Irrelevant Columns:")
print(df.columns)

print("\nDataFrame Before Dropping Columns:")
print(df_before_drop.columns)

print("\nMemory Usage After Dropping Columns:")
print(df.memory_usage().sum() / (1024 ** 2), "MB")