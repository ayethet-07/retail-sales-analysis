import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load real dataset (download retail_sales.csv from Kaggle and place in /data)
df = pd.read_csv('data/retail_sales.csv')

# If no real data yet, uncomment to generate sample (for testing)
# np.random.seed(42)
# dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
# data = {
#     'Transaction ID': range(1, 366),
#     'Date': dates,
#     'Customer ID': np.random.choice(['C' + str(i) for i in range(100)], 365),
#     'Gender': np.random.choice(['Male', 'Female'], 365),
#     'Age': np.random.randint(18, 70, 365),
#     'Product Category': np.random.choice(['Electronics', 'Clothing', 'Beauty', 'Books'], 365),
#     'Quantity': np.random.randint(1, 5, 365),
#     'Price per Unit': np.random.choice([10, 20, 50, 100, 200], 365),
# }
# data['Total Amount'] = [q * p for q, p in zip(data['Quantity'], data['Price per Unit'])]
# df = pd.DataFrame(data)
# df.to_csv('data/sample_retail_sales.csv', index=False)

# Basic EDA
print(df.head())
print(df.describe())
print(df.info())

# Sales trends over time
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
monthly_sales = df['Total Amount'].resample('ME').sum()  # Use 'ME' for month-end
plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title('Monthly Sales Trends')
plt.savefig('images/monthly_sales.png')

# Sales by category
category_sales = df.groupby('Product Category')['Total Amount'].sum()
plt.figure(figsize=(8,4))
category_sales.plot(kind='bar')
plt.title('Sales by Product Category')
plt.savefig('images/category_sales.png')

# Customer demographics
sns.boxplot(x='Gender', y='Age', data=df)
plt.title('Age Distribution by Gender')
plt.savefig('images/age_gender.png')

print('Analysis complete. Plots saved in /images.')
