import pandas as pd
import matplotlib.pyplot as plt

inventory = pd.read_csv("../data/cleaned/inventory_cleaned.csv")

print(inventory.head())

print(inventory.describe())

plt.figure(figsize=(8,5))

plt.hist(inventory["Stock"],bins=20)

plt.title("Stock Distribution")

plt.xlabel("Stock")

plt.ylabel("Frequency")

plt.show()