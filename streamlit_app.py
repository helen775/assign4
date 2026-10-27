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

# Create 5 pink petals and 1 yellow center
data = pd.DataFrame({
    "x": [2, 2, 1.81, 1.88, 2.12, 2.19],
    "y": [2.22, 2, 2.07, 1.82, 1.82, 2.07],
    "size": [3200, 1400, 3200, 3200, 3200, 3200],
    "color": ["#FF69B4", "#FFD700", "#FF69B4",
              "#FF69B4", "#FF69B4", "#FF69B4"]
})

# Draw the flower
st.vega_lite_chart(data, {
    "width": 350,
    "height": 350,
    "mark": {"type": "circle"},
    "encoding": {
        "x": {
            "field": "x",
            "type": "quantitative",
            "scale": {"domain": [1.5, 2.5]},
            "axis": None
        },
        "y": {
            "field": "y",
            "type": "quantitative",
            "scale": {"domain": [1.5, 2.5]},
            "axis": None
        },
        "size": {
            "field": "size",
            "type": "quantitative",
            "scale": {"domain": [0, 3200], "range": [0, 3200]},
            "legend": None
        },
        "color": {
            "field": "color",
            "type": "nominal",
            "scale": None,
            "legend": None
        }
    }
})
