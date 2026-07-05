import pandas as pd

df = pd.read_csv("data/generated/sales.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df.to_csv("data/cleaned/sales_cleaned.csv", index=False)

print("Sales cleaned successfully!")