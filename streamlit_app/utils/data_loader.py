import pandas as pd

def load_data():
    sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
    customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
    transactions = pd.read_csv("data/cleaned/transactions_cleaned.csv")

    return sales, customers, transactions