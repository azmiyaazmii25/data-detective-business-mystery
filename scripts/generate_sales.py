import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

sales = []

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

for i in range(1, 50001):

    customer = random.randint(1, 10000)
    product = random.randint(1, 200)
    employee = random.randint(1, 300)
    store = random.randint(1, 50)

    quantity = random.randint(1, 5)

    price = random.randint(300, 50000)

    discount = random.choice([0, 5, 10, 15, 20])

    revenue = quantity * price * (1 - discount / 100)

    cost = revenue * random.uniform(0.55, 0.80)

    profit = revenue - cost

    sales.append({

        "SaleID": f"SALE{i:05}",

        "CustomerID": customer,

        "ProductID": product,

        "EmployeeID": f"EMP{employee:03}",

        "StoreID": f"S{store:03}",

        "Date": fake.date_between("-2y", "today"),

        "Quantity": quantity,

        "Price": price,

        "Discount": discount,

        "Revenue": round(revenue, 2),

        "Profit": round(profit, 2),

        "PaymentMode": random.choice(payment_modes)

    })

df = pd.DataFrame(sales)

df.to_csv(
    "data/generated/sales.csv",
    index=False
)

print("Sales Dataset Generated Successfully!")