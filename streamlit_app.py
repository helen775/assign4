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
st.title("Drawing a Cloud ☁️")


import streamlit as st

# Display the title
st.title("Drawing a Candle 🕯️")

# Draw a candle using HTML and CSS
st.markdown("""
<div style="display: flex; flex-direction: column;
            align-items: center;">

    <!-- Flame -->
    <div style="width: 30px; height: 45px;
                background-color: orange;
                border-radius: 50% 50% 50% 0;
                transform: rotate(-45deg);">
    </div>

    <!-- Wick -->
    <div style="width: 5px; height: 15px;
                background-color: black;">
    </div>

    <!-- Candle Body -->
    <div style="width: 80px; height: 180px;
                background-color: pink;
                border-radius: 5px;">
    </div>

</div>
""", unsafe_allow_html=True)

