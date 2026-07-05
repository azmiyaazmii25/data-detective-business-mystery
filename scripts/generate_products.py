import pandas as pd
import random

categories = [

"Electronics",

"Clothing",

"Home Appliances",

"Kitchen",

"Accessories"

]

products=[]

for i in range(1,201):

    products.append({

        "ProductID":i,

        "ProductName":"Product "+str(i),

        "Category":random.choice(categories),

        "Price":random.randint(300,50000),

        "Cost":random.randint(200,30000)

    })

df=pd.DataFrame(products)

df.to_csv("data/generated/products.csv",index=False)

print("Products Generated")