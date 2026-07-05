import pandas as pd
import matplotlib.pyplot as plt

txn = pd.read_csv("../data/cleaned/transactions_cleaned.csv")

print(txn.head())

print(txn["Fraud"].value_counts())

txn["Fraud"].value_counts().plot(kind="pie",autopct="%1.1f%%")

plt.ylabel("")

plt.title("Fraud Distribution")

plt.show()