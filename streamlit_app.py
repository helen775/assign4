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


import streamlit as st

# Display the title
st.title("Drawing a Candle 🕯️")

# Draw the candle
st.vega_lite_chart({
    "width": 250,
    "height": 350,
    "layer": [
        # Pink rectangular candle body
        {
            "mark": {"type": "rect", "color": "pink"},
            "encoding": {
                "x": {"datum": 1},
                "x2": {"datum": 3},
                "y": {"datum": 0},
                "y2": {"datum": 4}
            }
        },
        # Black wick
        {
            "mark": {"type": "rect", "color": "black"},
            "encoding": {
                "x": {"datum": 1.95},
                "x2": {"datum": 2.05},
                "y": {"datum": 4},
                "y2": {"datum": 4.5}
            }
        },
        # Orange flame
        {
            "mark": {"type": "point", "filled": True,
                     "color": "orange", "size": 1000},
            "encoding": {
                "x": {"datum": 2},
                "y": {"datum": 5}
            }
        }
    ]
})


