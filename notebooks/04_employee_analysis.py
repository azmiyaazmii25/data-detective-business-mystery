import pandas as pd
import matplotlib.pyplot as plt

emp = pd.read_csv("../data/cleaned/employees_cleaned.csv")

print(emp.head())

print(emp["Role"].value_counts())

plt.figure(figsize=(9,5))

emp["Role"].value_counts().plot(kind="bar")

plt.title("Employees by Role")

plt.tight_layout()

plt.show()