
import streamlit as st
import pandas as pd
pip install -r requirements.txt
# Load the full patterns CSV
@st.cache_data
def load_data():
    return pd.read_csv("patterns.csv")

df = load_data()

st.title("Serdal Pattern Intelligence")

# Filter
selected_pattern = st.selectbox("Choose Pattern ID", df["PatternID"].unique())

pattern_data = df[df["PatternID"] == selected_pattern].iloc[0]

st.subheader("Market Insights")
st.write(f"**QoQ_Price:** {pattern_data['QoQ_Price']}")
st.write(f"**YoY_Price:** {pattern_data['YoY_Price']}")
st.write(f"**QoQ_Volume:** {pattern_data['QoQ_Volume']}")
st.write(f"**YoY_Volume:** {pattern_data['YoY_Volume']}")
st.write(f"**Offplan_Level:** {pattern_data['Offplan_Level']}")

st.markdown("### 🔍 Insight Narrative")
st.info(pattern_data["Insight_Narrative"])

st.markdown("### 💡 End-User Advice")
st.success(pattern_data["EndUser_Advice"])

st.markdown("### 💼 Investor Advice")
st.warning(pattern_data["Investor_Advice"])
