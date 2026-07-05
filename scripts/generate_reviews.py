from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

reviews = []

sentiments = [
    "Positive",
    "Neutral",
    "Negative"
]

for i in range(1, 15001):

    rating = random.randint(1, 5)

    reviews.append({

        "ReviewID": f"REV{i:05}",

        "CustomerID": random.randint(1, 10000),

        "Rating": rating,

        "Review": fake.sentence(),

        "Sentiment": random.choice(sentiments),

        "FakeReview": random.choice(["Yes"] * 2 + ["No"] * 98)

    })

df = pd.DataFrame(reviews)

df.to_csv(
    "data/generated/reviews.csv",
    index=False
)

print("Reviews Dataset Generated Successfully!")