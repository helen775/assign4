# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Helen Chen")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart","🎀Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT") ## display title of tab 
    st.dataframe(df, use_container_width=True) 

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close']) # display line chart

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT") 
    st.bar_chart(df['Volume'])
    
# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"Something New")

# Display the title
st.title("Drawing a Candle 🕯️")

# Create points for the candle
data = pd.DataFrame({
    "x": [2, 2, 2, 2, 2, 2],
    "y": [1, 2, 3, 4, 5, 6],
    "size": [1500, 1500, 1500, 1500, 200, 500],
    "color": ["pink", "pink", "pink", "pink", "black", "orange"]
})

# Draw the candle
st.scatter_chart(
    data,
    x="x",
    y="y",
    size="size",
    color="color"
)


