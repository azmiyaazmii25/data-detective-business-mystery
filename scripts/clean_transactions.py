import pandas as pd

df = pd.read_csv("data/generated/transactions.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["TransactionDate"] = pd.to_datetime(df["TransactionDate"])

df.to_csv("data/cleaned/transactions_cleaned.csv", index=False)

print("Transactions cleaned successfully!")