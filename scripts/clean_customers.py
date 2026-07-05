import pandas as pd

df = pd.read_csv("data/generated/customers.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Convert JoinDate
df["JoinDate"] = pd.to_datetime(df["JoinDate"])

# Save cleaned data
df.to_csv("data/cleaned/customers_cleaned.csv", index=False)

print("Customers cleaned successfully!")