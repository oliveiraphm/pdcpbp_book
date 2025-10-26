import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

# Sample dataset
data = {
    'Customer ID': [1, 2, 3, 4, 5],
    'Contract Type': ['Month-to-Month', 'One Year', 'Month-to-Month', 'Two Year', 'One Year'],
    'Internet Service': ['DSL', 'Fiber Optic', 'DSL', 'Fiber Optic', 'No Internet Service'],
    'Payment Method': ['Electronic Check', 'Mailed Check', 'Bank Transfer', 'Credit Card', 'Electronic Check'],
}

df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.countplot(x='Contract Type', data=df).set_title('Contract Type Distribution')
plt.show()

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded_columns = one_hot_encoder.fit_transform(df[['Contract Type']])

encoded_df = pd.DataFrame(encoded_columns, columns=one_hot_encoder.get_feature_names_out(['Contract Type']))

df_encoded = pd.concat([df, encoded_df], axis=1)

df_encoded = df_encoded.drop(['Contract Type'], axis=1)

print(df_encoded)

encoded_cols = encoded_df.columns

fig, axes = plt.subplots(1, len(encoded_cols), figsize=(6 * len(encoded_cols), 5))
for i, col in enumerate(encoded_cols):
    sns.countplot(ax=axes[i], x=encoded_df[col]).set_title(f'{col} Distribution')
plt.tight_layout()
plt.show()