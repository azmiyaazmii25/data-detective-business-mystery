from faker import Faker
import pandas as pd
import random

fake = Faker("en_IN")

customers = []

regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

for i in range(1,10001):

    customers.append({

        "CustomerID":i,

        "Name":fake.name(),

        "Age":random.randint(18,70),

        "Gender":random.choice(["Male","Female"]),

        "Region":random.choice(regions),

        "City":fake.city(),

        "Email":fake.email(),

        "JoinDate":fake.date_between("-5y","today")

    })

df=pd.DataFrame(customers)

df.to_csv("data/generated/customers.csv",index=False)

print("Customers Generated Successfully!")