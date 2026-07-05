import streamlit as st
import pandas as pd

st.title("🕵️ Investigation Cases")

# -----------------------------
# INIT SESSION STATE (IMPORTANT FIX)
# -----------------------------
if "level" not in st.session_state:
    st.session_state.level = 1

# LOAD DATA
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
transactions = pd.read_csv("data/cleaned/transactions_cleaned.csv")

df = sales.merge(customers, on="CustomerID", how="left")

# -----------------------------
# CASE SELECTION
# -----------------------------
case = st.selectbox(
    "Select Case",
    ["Sales Drop", "Fraud Detection", "Inventory Theft"]
)

# -----------------------------
# CASE 1
# -----------------------------
if case == "Sales Drop":
    st.subheader("📉 Sales Drop Analysis")

    result = df.groupby("Region")["Revenue"].sum().sort_values()

    st.dataframe(result)

# -----------------------------
# CASE 2 (FIXED UNLOCK)
# -----------------------------
elif case == "Fraud Detection":

    if st.session_state.level >= 2:
        st.subheader("🚨 Fraud Detection Case")

        fraud = transactions[transactions["Fraud"] == "Yes"]

        st.dataframe(fraud)

        st.success(f"Total Fraud Cases: {len(fraud)}")

    else:
        st.warning("🔒 Complete Level 2 in Game Mode to unlock this case!")

# -----------------------------
# CASE 3 (FIXED UNLOCK)
# -----------------------------
elif case == "Inventory Theft":

    if st.session_state.level >= 3:
        st.subheader("📦 Inventory Theft Case")

        st.info("Analyzing stock mismatches and missing inventory patterns...")

    else:
        st.warning("🔒 Complete Level 3 in Game Mode to unlock this case!")