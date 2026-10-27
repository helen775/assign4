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
st.title("Drawing a Flower 🌸")

# Create points for the flower
data = pd.DataFrame({
    "x": [2.0, 2.0, 1.7, 2.3, 1.8, 2.2],
    "y": [2.0, 2.35, 2.15, 2.15, 1.75, 1.75],
    "size": [900, 1400, 1400, 1400, 1400, 1400],
    "color": ["yellow", "pink", "pink", "pink", "pink", "pink"]
})

# Draw the flower
st.scatter_chart(
    data,
    x="x",
    y="y",
    size="size",
    color="color"
)



