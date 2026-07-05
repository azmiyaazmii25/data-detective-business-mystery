import pandas as pd

df = pd.read_csv("data/generated/inventory.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.to_csv("data/cleaned/inventory_cleaned.csv", index=False)

print("Inventory cleaned successfully!")