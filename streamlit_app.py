# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Helen Chen")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart","🎀 Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])
    
# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"Something New")
    st.bar_chart(df['Volume'])

import matplotlib.pyplot as plt


        # Set up the app title
        st.title("Static Circle Display")

        # Create a matplotlib figure and axis
        fig, ax = plt.subplots()

        # Create a circle at center (0,0) with a radius of 1
        circle = plt.Circle((0, 0), radius=1, color="blue", fill=True)

        # Add the circle to the axis
        ax.add_patch(circle)

        # Set limits and ensure the aspect ratio is equal so the circle isn't distorted
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect("equal")

        # Turn off the axis lines and labels for a cleaner look
        ax.axis("off")

        # Display the plot in the Streamlit app
        st.pyplot(fig)

