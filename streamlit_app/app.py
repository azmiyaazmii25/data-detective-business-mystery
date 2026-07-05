import streamlit as st
import pandas as pd
import plotly.express as px
from utils.scoring import get_rank

st.set_page_config(page_title="Data Detective", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
h1, h2, h3 { color: #00ffcc; }
.stButton button {
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION INIT ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "q_index" not in st.session_state:
    st.session_state.q_index = 0


# ---------------- DATA LOAD ----------------
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
transactions = pd.read_csv("data/cleaned/transactions_cleaned.csv")

df = sales.merge(customers, on="CustomerID", how="left")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🕵️ Detective Panel")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Dashboard", "🕵️ Cases", "🎮 Game"]
)

st.sidebar.divider()
st.sidebar.write(f"⭐ Score: {st.session_state.score}")
st.sidebar.write(f"🎮 Level: {st.session_state.level}")
st.sidebar.write(f"🏆 Rank: {get_rank(st.session_state.score)}")


# ---------------- HOME ----------------
if page == "🏠 Home":
    st.title("🕵️ Data Detective: Business Mystery Game")

    st.markdown("""
    ### 🎬 Story
    A company is facing:
    - 📉 Sales drop
    - 🚨 Fraud transactions
    - 📦 Inventory mismatch

    ### 🎯 Mission
    Solve cases using data analysis.

    👉 Go to GAME to unlock cases.
    """)


# ---------------- DASHBOARD ----------------
elif page == "📊 Dashboard":
    st.title("📊 Business Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Revenue", df["Revenue"].sum())
    col2.metric("Profit", df["Profit"].sum())
    col3.metric("Orders", len(df))

    fig = px.bar(
        df.groupby("Region")["Revenue"].sum().reset_index(),
        x="Region",
        y="Revenue",
        title="Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)


# ---------------- CASES (UNLOCKED BY LEVEL) ----------------
elif page == "🕵️ Cases":
    st.title("🕵️ Investigation Cases")

    case = st.selectbox(
        "Select Case",
        ["Sales Drop", "Fraud Detection", "Inventory Theft"]
    )

    # CASE 1 ALWAYS OPEN
    if case == "Sales Drop":
        st.subheader("📉 Sales Drop Analysis")
        st.dataframe(df.groupby("Region")["Revenue"].sum().sort_values())

    # CASE 2 LEVEL LOCK
    elif case == "Fraud Detection":
        if st.session_state.level >= 2:
            st.subheader("🚨 Fraud Detection Case")
            fraud = transactions[transactions["Fraud"] == "Yes"]
            st.dataframe(fraud)
            st.success(f"Fraud Cases: {len(fraud)}")
        else:
            st.warning("🔒 Reach LEVEL 2 in GAME to unlock Fraud Case")

    # CASE 3 LEVEL LOCK
    elif case == "Inventory Theft":
        if st.session_state.level >= 3:
            st.subheader("📦 Inventory Theft Case")
            st.info("Inventory mismatch analysis unlocked!")
        else:
            st.warning("🔒 Reach LEVEL 3 in GAME to unlock Inventory Case")


# ---------------- GAME (ONLY ONE GAME PAGE) ----------------
elif page == "🎮 Game":
    st.title("🎮 Detective Game Mode")

    merged = sales.merge(customers, on="CustomerID", how="left")

    # ---------------- FUNCTIONS ----------------
    def lowest_region():
        return merged.groupby("Region")["Revenue"].sum().idxmin()

    def highest_payment():
        return sales.groupby("PaymentMode")["Revenue"].sum().idxmax()

    def fraud_range():
        f = len(transactions[transactions["Fraud"] == "Yes"])
        if f < 50: return "0-50"
        elif f < 100: return "50-100"
        elif f < 500: return "100-500"
        else: return "500+"

    # ---------------- QUESTIONS ----------------
    questions = [
        {
            "q": "Which region has lowest sales?",
            "options": merged["Region"].dropna().unique().tolist(),
            "answer": lowest_region()
        },
        {
            "q": "Which payment mode gives highest revenue?",
            "options": sales["PaymentMode"].unique().tolist(),
            "answer": highest_payment()
        },
        {
            "q": "Fraud transaction range?",
            "options": ["0-50", "50-100", "100-500", "500+"],
            "answer": fraud_range()
        }
    ]

    # ---------------- PROGRESS ----------------
    progress = st.session_state.q_index / len(questions)
    st.progress(progress)

    # ---------------- GAME LOGIC ----------------
    if st.session_state.q_index < len(questions):

        q = questions[st.session_state.q_index]

        st.subheader(q["q"])

        ans = st.radio("Select answer:", q["options"])

        if st.button("Submit"):

            if ans == q["answer"]:
                st.session_state.score += 20
                st.success("Correct!")
            else:
                st.session_state.score -= 10
                st.error(f"Wrong! Correct: {q['answer']}")

            st.session_state.q_index += 1

            # 🔥 LEVEL PROGRESSION FIX
            if st.session_state.q_index == 1:
                st.session_state.level = 1
            elif st.session_state.q_index == 2:
                st.session_state.level = 2
            elif st.session_state.q_index >= 3:
                st.session_state.level = 3

            st.rerun()

    else:
        st.balloons()

        st.title("🏁 FINAL DETECTIVE REPORT")

        st.success("All cases solved!")

        st.write(f"⭐ Score: {st.session_state.score}")
        st.write(f"🏆 Rank: {get_rank(st.session_state.score)}")

        st.info("Cases unlocked based on level progression")

        if st.button("Restart Game"):
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.session_state.level = 1
            st.rerun()