import pandas as pd
import random

inventory = []

for product in range(1, 201):

    for store in range(1, 51):

        stock = random.randint(50, 500)

        inventory.append({

            "ProductID": product,

            "StoreID": f"S{store:03}",

            "Stock": stock,

            "ReorderLevel": random.randint(20, 80),

            "DamagedStock": random.randint(0, 15),

            "LostStock": random.randint(0, 10)

        })

df = pd.DataFrame(inventory)

df.to_csv(
    "data/generated/inventory.csv",
    index=False
)

print("Inventory Dataset Generated Successfully!")