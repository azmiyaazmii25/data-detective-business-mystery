import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned/customers_cleaned.csv")

print(df.head())

print(df.info())

print(df.describe())

print("\nTotal Customers:", len(df))

print("\nCustomers by Region")

print(df["Region"].value_counts())

plt.figure(figsize=(8,5))

df["Region"].value_counts().plot(kind="bar")

plt.title("Customers by Region")

plt.xlabel("Region")

plt.ylabel("Customers")

plt.tight_layout()

plt.show()