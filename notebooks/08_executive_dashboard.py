import pandas as pd

customers = pd.read_csv("../data/cleaned/customers_cleaned.csv")
sales = pd.read_csv("../data/cleaned/sales_cleaned.csv")
products = pd.read_csv("../data/cleaned/products_cleaned.csv")
employees = pd.read_csv("../data/cleaned/employees_cleaned.csv")

print("="*40)

print("EXECUTIVE KPI DASHBOARD")

print("="*40)

print("Total Customers :",len(customers))

print("Total Employees :",len(employees))

print("Total Products :",len(products))

print("Total Sales :",len(sales))

print("Total Revenue : ₹",round(sales["Revenue"].sum(),2))

print("Total Profit : ₹",round(sales["Profit"].sum(),2))

print("Average Revenue : ₹",round(sales["Revenue"].mean(),2))

print("="*40)