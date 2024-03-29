# -*- coding: utf-8 -*-
"""LVADSUSR118-Siddharth_FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HZ0E2R7XpTP_m3BNAE77WOOl8o8d05K8
"""

#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_excel('Walmart_Dataset Python_Final_Assessment.xlsx')
print(df.describe())
print(df.info())

#2

print(df.isnull().sum())
duplicate_rows = df[df.duplicated()]
print("Duplicate Rows:", duplicate_rows)
df.drop_duplicates()

#3

df.describe()

#4

plt.hist(df['Sales'], bins=20)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Distribution of Sales')
plt.show()

sns.boxplot(x='Profit', data=df)
plt.title('Box plot for Profit')
plt.show()

plt.scatter(df['Sales'], df['Profit'])
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Scatter plot of Sales vs Profit')
plt.show()

sns.barplot(x='Category',y='Sales',data=df)
plt.xlabel('Categories')
plt.ylabel('Sales')
plt.title('Sales by category')
plt.show()

sns.lineplot(y='Profit',x='Order Date' ,data=df)
plt.xlabel('Order date')
plt.ylabel('Profit')
plt.title('Profit based on order date')
plt.show()

df.plot(kind='scatter', x='Sales', y='Quantity', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

#5
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='cool')
plt.title('Correlation Matrix between sales, quantity and profit')
plt.show()

#6

sns.boxplot(data=df)

# Using Z-score for finding outliers
z1 = np.abs((df['Sales'] - df['Sales'].mean()) / df['Sales'].std())
outliers = df[z1 > 3]
print("Outliers according to sales:", outliers)

z2 = np.abs((df['Quantity'] - df['Quantity'].mean()) / df['Quantity'].std())
outliers1 = df[z2 > 3]
print("Outliers according to quantity:", outliers1)

#7
#trend analysis
df['Order Year'] = pd.to_datetime(df['Order Date']).dt.year


yearly_s_p = df.groupby('Order Year').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

# Visualize sales and profit trends over the years
plt.figure(figsize=(8, 5))
plt.plot(yearly_s_p['Order Year'], yearly_s_p['Sales'], label='Total Sales')
plt.plot(yearly_s_p['Order Year'], yearly_s_p['Profit'], label='Total Profit')
plt.xlabel('Year')
plt.ylabel('Total Amount')
plt.title('Sales and Profit Trend Over Years')
plt.legend()
plt.grid(True)
plt.show()

#trend analysis

category_sales = df.groupby(['Order Year', 'Category'])['Sales'].sum().unstack()
category_growth = category_sales.pct_change(axis=0) * 100

max_cat = category_growth.mean().idxmax()
max_p = category_growth.mean().max()

print("The Product Category which has the Highest Percentage Growth is :")
print("Category:", max_cat)
print("The Average Percentage Growth is:", max_p)

#customer analysis

df['Order Date'] = pd.to_datetime(df['Order Date'])

customer_group = df.groupby('EmailID')

customer_orders_sales = customer_group.agg({'Order ID': 'nunique', 'Sales': 'sum'}).reset_index()
customer_orders_sales.columns = ['EmailID', 'Number of Orders', 'Total Sales']

top_orders = customer_orders_sales.nlargest(5, 'Number of Orders')
top_sales = customer_orders_sales.nlargest(5, 'Total Sales')

print("The Top 5 Customers based on Number of Orders are:")
print(top_orders)
print("\n The Top 5 Customers based on Total Sales are:")
print(top_sales)

#customer analysis

df_sorted = df.sort_values(['EmailID', 'Order Date'])
df_sorted['Time Between Orders'] = df_sorted.groupby('EmailID')['Order Date'].diff()

average_time_between_orders = df_sorted.groupby('EmailID')['Time Between Orders'].mean().reset_index()
average_time_between_orders.columns = ['EmailID', 'Average Time Between Orders']

print("\nAverage Time Between Orders for Each Customer:")
print(average_time_between_orders)


# we observe different patterns of repeat orders based on average order time

#comprehensive analytics

#Optimizing Supply Chain based on Sales Velocity and Order Fulfillment Data:

# We can build a strong model to predict stock renewal needs. It would indicate when we should place an order.
# We can also predict the demand.
# we can understand customer needs to figure out the inventory stick levels.
# Better time planning can help us in avoiding delays.
# we can  use data analytics to optimize logistics  and reduce delays and transportation costs.
#Geographic distribution of sales.

#It is affected by a lot of conditions such as socio economic issues.
# What is popular in what region varies. We should take in account local trends.
# We can do personalized marketing based on a region after identifying preferences.
# we can utilize geospatial analytics to identify areas with high sales potential and tailor marketing campaigns accordingly.
# we can implement location-based marketing strategies, such as targeted advertisements or promotions based on the customer's proximity to a store or distribution center.
# we can leverage social media to reach specific geographic segments effectively.

#
#High value customers

# we can use historical data to find out high value customers. This is also affected by seasonal expenditure.
# We shoulld look into the order quanity , order frequencya, and spend amount to find out high customers
# we can look into patterns in customer behaviour.
# People who are high valued can be attracted by coupons or loyalty programs
# we can use strategies like VIP clubs, premium offers, and personalized recommendations.