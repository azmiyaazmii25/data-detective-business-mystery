import pandas as pd

df = pd.read_csv("data/generated/reviews.csv")

df.drop_duplicates(inplace=True)

df.dropna(inplace=True)

df.to_csv("data/cleaned/reviews_cleaned.csv", index=False)

print("Reviews cleaned successfully!")