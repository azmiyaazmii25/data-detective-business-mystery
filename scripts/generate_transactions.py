from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

transactions = []

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

for i in range(1, 50001):

    fraud = "No"

    if random.random() < 0.01:
        fraud = "Yes"

    transactions.append({

        "TransactionID": f"TXN{i:05}",

        "Amount": random.randint(200, 100000),

        "PaymentMethod": random.choice(payment_methods),

        "Location": fake.city(),

        "Device": random.choice(["Android", "iPhone", "Laptop"]),

        "TransactionDate": fake.date_between("-2y", "today"),

        "Fraud": fraud

    })

df = pd.DataFrame(transactions)

df.to_csv(
    "data/generated/transactions.csv",
    index=False
)

print("Transactions Dataset Generated Successfully!")