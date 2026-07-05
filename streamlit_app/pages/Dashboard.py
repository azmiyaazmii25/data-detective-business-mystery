import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Business Intelligence Dashboard")

# Load data
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹ {sales['Revenue'].sum():,.0f}")
col2.metric("Total Profit", f"₹ {sales['Profit'].sum():,.0f}")
col3.metric("Total Orders", len(sales))

st.divider()

# Revenue by Region
fig1 = px.bar(
    sales.groupby("StoreID")["Revenue"].sum().reset_index(),
    x="StoreID",
    y="Revenue",
    title="Revenue by Store"
)
st.plotly_chart(fig1, use_container_width=True)

# Payment Mode Analysis
fig2 = px.pie(
    sales,
    names="PaymentMode",
    values="Revenue",
    title="Revenue by Payment Mode"
)
st.plotly_chart(fig2, use_container_width=True)