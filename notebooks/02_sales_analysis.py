import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("../data/cleaned/sales_cleaned.csv")

print(sales.head())

print("Total Revenue")

print(sales["Revenue"].sum())

print("Total Profit")

print(sales["Profit"].sum())

print("Average Order Value")

print(sales["Revenue"].mean())

plt.figure(figsize=(10,5))

sales.groupby("PaymentMode")["Revenue"].sum().plot(kind="bar")

plt.title("Revenue by Payment Mode")

plt.ylabel("Revenue")

plt.tight_layout()

plt.show()