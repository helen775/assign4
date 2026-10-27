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
        
        # Create points that form a cloud
        data = pd.DataFrame({
            "x": [1, 2, 3, 4, 5, 6, 7],
            "y": [2, 3, 4, 4, 4, 3, 2],
            "size": [800, 2000, 3000, 3500, 3000, 2000, 800]
        })
        
        # Draw the cloud using a scatter chart
        st.scatter_chart(
            data,
            x="x",
            y="y",
            size="size",
            color="#87CEEB"
        )

