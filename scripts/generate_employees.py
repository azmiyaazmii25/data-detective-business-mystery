from faker import Faker
import pandas as pd
import random

# Create Faker object for Indian names
fake = Faker("en_IN")

# List to store employee records
employees = []

# Company regions
regions = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

# Employee roles
roles = [
    "Store Manager",
    "Sales Executive",
    "Cashier",
    "Warehouse Staff"
]

# Salary range for each role
salary = {
    "Store Manager": (55000, 80000),
    "Sales Executive": (25000, 45000),
    "Cashier": (20000, 35000),
    "Warehouse Staff": (18000, 32000)
}

# Generate 300 employees
for i in range(1, 301):

    role = random.choice(roles)

    employees.append({

        "EmployeeID": f"EMP{i:03}",

        "Name": fake.name(),

        "Gender": random.choice(["Male", "Female"]),

        "Age": random.randint(21, 58),

        "Role": role,

        "StoreID": f"S{random.randint(1,50):03}",

        "Region": random.choice(regions),

        "Salary": random.randint(
            salary[role][0],
            salary[role][1]
        ),

        "JoiningDate": fake.date_between("-10y", "today"),

        "PerformanceScore": round(
            random.uniform(2.5,5.0),2
        ),

        "IsSuspect":"No"

    })

# Secret detective clue
suspect = random.randint(0,299)

employees[suspect]["Role"]="Warehouse Staff"

employees[suspect]["IsSuspect"]="Yes"

# Convert list into DataFrame
df = pd.DataFrame(employees)

# Save CSV
df.to_csv(
    "data/generated/employees.csv",
    index=False
)

print("Employees Generated Successfully!")