import pandas as pd

df = pd.read_csv("data/generated/products.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.to_csv("data/cleaned/products_cleaned.csv", index=False)

print("Products cleaned successfully!")