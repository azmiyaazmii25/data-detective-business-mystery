# 🕵️ Data Detective: Business Mystery Challenge

**An interactive data analytics game where you solve real-world business mysteries with data — not just stare at dashboards.**

---

> 🆕 **Something new I tried:** Most data analytics projects end at a dashboard. This one turns the analysis into a **game** — built entirely in Streamlit, with levels, scoring, and a detective storyline layered on top of real business data. It was my first attempt at combining game mechanics with a BI tool, and honestly one of the most fun things I've built.

---

## 🎯 Overview

A retail company is in trouble. Sales have dropped, fraud is creeping in, inventory numbers don't add up, and customer behavior is shifting.

You are the **Data Detective Analyst**. Your job: dig into the datasets, spot the patterns, and crack the case.

**The mysteries you'll investigate:**
- 📉 Sudden sales drop
- 🚨 Fraudulent transactions
- 📦 Inventory mismatches
- 🧾 Customer behavior anomalies

---

## 🎮 Key Features

| Feature | Description |
|---|---|
| 🕵️ Detective-style gameplay | Investigate cases through an interactive narrative |
| 📊 BI Dashboard | Real business intelligence visuals, not static charts |
| 📈 KPIs | Revenue, Profit, Orders tracked live |
| 🔓 Level-based unlocking | Progress through cases as you solve them |
| 🚨 Fraud detection simulation | Spot suspicious transactions |
| 📦 Inventory analysis | Reconcile mismatches in stock data |
| 🏆 Score + Rank system | Climb from Rookie to Senior Analyst |
| 🎨 Dark detective theme | Immersive noir-style UI |

---

## 🛠️ Tech Stack

`Python` · `Pandas` · `Streamlit` · `Plotly` · `NumPy` · CSV-based datasets

---

## 📂 Project Structure

```
data-detective-business-mystery/
├── data/
│   ├── cleaned/                    # Final cleaned datasets
│   ├── generated/                  # Synthetically generated raw data
│   └── raw/                        # Original/raw source data
│
├── notebooks/                      # EDA & analysis scripts
│   ├── 01_customer_analysis.py
│   ├── 02_sales_analysis.py
│   ├── 03_product_analysis.py
│   ├── 04_employee_analysis.py
│   ├── 05_inventory_analysis.py
│   ├── 06_reviews_analysis.py
│   ├── 07_transaction_analysis.py
│   └── 08_executive_dashboard.py
│
├── scripts/                        # Data generation & cleaning pipeline
│   ├── generate_customers.py
│   ├── generate_employees.py
│   ├── generate_inventory.py
│   ├── generate_products.py
│   ├── generate_reviews.py
│   ├── generate_sales.py
│   ├── generate_transactions.py
│   ├── clean_customers.py
│   ├── clean_employees.py
│   ├── clean_inventory.py
│   ├── clean_products.py
│   ├── clean_reviews.py
│   ├── clean_sales.py
│   ├── clean_transactions.py
│   └── sql/                        # SQL scripts for data ops
│
├── streamlit_app/                  # Main application
│   ├── pages/
│   │   ├── Cases.py                # Case files & unlockable levels
│   │   ├── Dashboard.py            # BI dashboard (KPIs, charts)
│   │   └── Play_Game.py            # Game mode logic
│   ├── utils/                      # Helper functions (scoring, data loading)
│   ├── app.py                      # App entry point (Home/story mode)
│   └── style.py                    # Custom dark theme styling
│
├── tableau/                        # Tableau workbooks/exports (if any)
├── requirements.txt                # Project dependencies
├── .gitignore
└── README.md
```
---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/your-username/data-detective-business-mystery.git
cd data-detective-business-mystery
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run streamlit_app/app.py
```

---

## 🧠 Game Flow

1. **Home** — Story mode sets the scene
2. **Game Mode** — Solve detective questions using real data
3. **Score & Unlock** — Earn points to unlock new levels:
   - 🔹 Level 1 → Sales Analysis
   - 🔹 Level 2 → Fraud Detection
   - 🔹 Level 3 → Inventory Investigation
4. **Cases Page** — Unlocks progressively as you level up

---

## 🏆 Ranking System

| Score Range | Rank |
|---|---|
| < 20 | 🟤 Rookie Analyst |
| < 50 | 🔵 Junior Analyst |
| < 100 | 🟢 Senior Analyst |

---

## 📊 Business Insights Covered

- Regional sales performance analysis
- Payment mode revenue breakdown
- Fraud transaction detection
- Inventory mismatch investigation

---

## 💡 What I Learned

- Data cleaning with Pandas
- Data merging & join concepts
- Building interactive dashboards
- Streamlit app development
- Business KPI analysis
- Game logic using session state

---

## 🚀 Future Improvements

- [ ] Machine learning–based fraud detection
- [ ] Real-time database integration
- [ ] Advanced dashboard visualizations
- [ ] User authentication system

---

## 👨‍💻 Author:

**Azmiya**


*Data Analytics | Python | Streamlit | Tableau*

🔗 [LinkedIn](your-linkedin-url-here) &nbsp;|&nbsp; 💻 [GitHub](your-github-url-here)