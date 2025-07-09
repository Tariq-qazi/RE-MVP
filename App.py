
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Serdal MVP – Real Estate Pattern Advisor")

# Load the pattern CSV
df = pd.read_csv("Pattern.csv")

# Display table and filters
st.sidebar.header("Filter Options")
pattern_id = st.sidebar.selectbox("Select Pattern ID", df['PatternID'].unique())
filtered_df = df[df['PatternID'] == pattern_id]

st.subheader("Pattern Insight")
st.write(filtered_df[["PatternID", "Insight Narrative", "Recommendation"]])
