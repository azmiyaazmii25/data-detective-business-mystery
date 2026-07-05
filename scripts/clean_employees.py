import pandas as pd

df = pd.read_csv("data/generated/employees.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])

df.to_csv("data/cleaned/employees_cleaned.csv", index=False)

print("Employees cleaned successfully!")