import streamlit as st
import pandas as pd
from utils.scoring import get_rank

# -----------------------------
# PAGE CONFIG STYLE
# -----------------------------
st.set_page_config(page_title="Data Detective Game", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }

        h1, h2, h3 {
            color: #00ffcc;
        }

        .stButton button {
            background-color: #00ffcc;
            color: black;
            border-radius: 8px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 Data Detective Challenge Mode")

# -----------------------------
# LOAD DATA
# -----------------------------
sales = pd.read_csv("data/cleaned/sales_cleaned.csv")
customers = pd.read_csv("data/cleaned/customers_cleaned.csv")
transactions = pd.read_csv("data/cleaned/transactions_cleaned.csv")

# -----------------------------
# MERGE DATA (FIX FOR REGION ERROR)
# -----------------------------
merged = sales.merge(customers, on="CustomerID", how="left")

# -----------------------------
# SESSION STATE
# -----------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

# -----------------------------
# BUSINESS LOGIC FUNCTIONS
# -----------------------------
def lowest_sales_region():
    return merged.groupby("Region")["Revenue"].sum().idxmin()

def highest_payment_mode():
    return sales.groupby("PaymentMode")["Revenue"].sum().idxmax()

def fraud_range():
    fraud_count = len(transactions[transactions["Fraud"] == "Yes"])
    if fraud_count < 50:
        return "0-50"
    elif fraud_count < 100:
        return "50-100"
    elif fraud_count < 500:
        return "100-500"
    else:
        return "500+"

# -----------------------------
# QUESTIONS
# -----------------------------
questions = [
    {
        "q": "Which region has the LOWEST sales?",
        "options": merged["Region"].dropna().unique().tolist(),
        "answer": lowest_sales_region()
    },
    {
        "q": "Which payment mode generates HIGHEST revenue?",
        "options": sales["PaymentMode"].unique().tolist(),
        "answer": highest_payment_mode()
    },
    {
        "q": "How many fraud transactions exist?",
        "options": ["0-50", "50-100", "100-500", "500+"],
        "answer": fraud_range()
    }
]

# -----------------------------
# PROGRESS BAR
# -----------------------------
total_questions = len(questions)
progress = st.session_state.q_index / total_questions

st.progress(progress)
st.write(f"Progress: {st.session_state.q_index}/{total_questions}")

# -----------------------------
# GAME LOGIC
# -----------------------------
if st.session_state.q_index < len(questions):

    q = questions[st.session_state.q_index]

    st.subheader(q["q"])

    choice = st.radio("Select answer:", q["options"])

    if st.button("Submit Answer"):

        if choice == q["answer"]:
            st.session_state.score += 20
            st.success("✅ Correct! +20 points")
        else:
            st.session_state.score -= 10
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")

        st.session_state.q_index += 1
        st.rerun()

else:
    st.balloons()

    st.title("🏁 CASE CLOSED REPORT")

    st.success("All detective cases have been solved successfully!")

    st.subheader("📊 Final Performance Summary")

    st.write(f"⭐ Final Score: {st.session_state.score}")
    st.write(f"🏆 Final Rank: {get_rank(st.session_state.score)}")

    if st.session_state.score >= 60:
        st.success("🕵️ Excellent Detective Work!")
    elif st.session_state.score >= 30:
        st.warning("🕵️ Good Analysis, but room for improvement.")
    else:
        st.error("🕵️ Needs more investigation skills.")

    st.info("💡 Recommendation: Focus on fraud patterns and sales trends.")

    if st.button("🔄 Restart Game"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.rerun()