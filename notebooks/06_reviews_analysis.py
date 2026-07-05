import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("../data/cleaned/reviews_cleaned.csv")

print(reviews.head())

print(reviews["Sentiment"].value_counts())

reviews["Sentiment"].value_counts().plot(kind="bar")

plt.title("Customer Sentiment")

plt.show()