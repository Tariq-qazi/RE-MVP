import streamlit as st
import pandas as pd

# Google Sheets public CSV link
sheet_url = "https://docs.google.com/spreadsheets/d/1R71kyvSYgRSMl8o4bfXhV9FH1N50D2uJ/export?format=csv"

st.set_page_config(page_title="Serdal PatternMatrix", layout="wide")

@st.cache_data(ttl=600)
def load_data():
    return pd.read_csv(sheet_url)

df = load_data()

st.title("🔍 Serdal PatternMatrix Dashboard")

# Filters
pattern_ids = df['PatternID'].dropna().unique()
selected_pattern = st.selectbox("Select Pattern ID", sorted(pattern_ids))

audience = st.radio("Select Audience View", ["Investor", "End-user"], horizontal=True)

# Filtered row
row = df[df['PatternID'] == selected_pattern].iloc[0]

# Show insight & recommendation
st.subheader("📌 Insight Narrative")
st.markdown(row['Insight Narrative'])

st.subheader("✅ Recommendation")
st.markdown(row['Recommendation'])

st.markdown(f"**Tags**: QoQ Price: `{row['QoQ_Price']}`, YoY Price: `{row['YoY_Price']}`, QoQ Volume: `{row['QoQ_Vol']}`, YoY Volume: `{row['YoY_Vol']}`, Offplan Level: `{row['Offplan_Level']}`")
