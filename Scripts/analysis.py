# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'supermarket_sales.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract additional time-related features
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.day_name()

# Exploratory Data Analysis (EDA)

# Total sales per branch
branch_sales = df.groupby('Branch')['Total'].sum().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='Branch', y='Total', data=branch_sales)
plt.title('Total Sales per Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.show()

# Sales by product line
product_sales = df.groupby('Product line')['Total'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Total', y='Product line', data=product_sales)
plt.title('Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.show()

# Sales trend over time
daily_sales = df.groupby('Date')['Total'].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['Date'], daily_sales['Total'])
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Sales by payment method
payment_sales = df['Payment'].value_counts().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='index', y='Payment', data=payment_sales)
plt.title('Sales by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Number of Transactions')
plt.show()

# Average rating by product line
product_rating = df.groupby('Product line')['Rating'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Rating', y='Product line', data=product_rating)
plt.title('Average Rating by Product Line')
plt.xlabel('Average Rating')
plt.ylabel('Product Line')
plt.show()
