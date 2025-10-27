import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from category_encoders import CountEncoder

data = {
    'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Books', 'Clothing', 'Electronics', 'Books', 'Clothing', 'Books'],
    'Total Purchases': [5, 2, 3, 8, 7, 4, 2, 5, 1, 6]
}

df = pd.DataFrame(data)

print("Sample Dataset:")
print(df)

X = df[['Customer ID', 'Product Category', 'Total Purchases']]

X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

count_encoder = CountEncoder(cols=['Product Category'])

X_train_encoded = count_encoder.fit_transform(X_train)

X_test_encoded = count_encoder.transform(X_test)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.countplot(ax=axes[0], x='Product Category', data=X_train).set_title('Original Product Category Distribution (Training Set)')

sns.countplot(ax=axes[1], x='Product Category', data=X_train_encoded).set_title('Encoded Product Category Distribution (Training Set)')

plt.tight_layout()
plt.show()

print("\n Encoded Training Dataset:")
print(X_train_encoded.head())

print("\nEncoded Testing Dataset:")
print(X_test_encoded.head())
