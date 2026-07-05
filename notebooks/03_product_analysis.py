import pandas as pd
import matplotlib.pyplot as plt

products = pd.read_csv("../data/cleaned/products_cleaned.csv")

print(products.head())

print(products["Category"].value_counts())

plt.figure(figsize=(8,5))

products["Category"].value_counts().plot(kind="pie",autopct="%1.1f%%")

plt.ylabel("")

plt.title("Products by Category")

plt.show()