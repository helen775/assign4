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
    
        # Import Matplotlib to draw the cookie
import matplotlib.pyplot as plt
        
# Display the title of the app
st.title("Chocolate Chip Cookie 🍪")
        
# Create a figure and axes for drawing
fig, ax = plt.subplots()
        
# Create a circular cookie with a light brown color
cookie = plt.Circle((0, 0), 1, color="burlywood")
        
# Add the cookie circle to the drawing
ax.add_patch(cookie)
        
# Define the positions of the chocolate chips
for x, y in [(-0.4, 0.3), (0.3, 0.5), (0, 0), (-0.5, -0.4), (0.5, -0.3)]:
        
# Draw a small dark brown circle at each position
ax.add_patch(plt.Circle((x, y), 0.12, color="saddlebrown"))
        
# Set the horizontal boundaries of the drawing
ax.set_xlim(-1.2, 1.2)
        
# Set the vertical boundaries of the drawing
ax.set_ylim(-1.2, 1.2)
        
# Keep the cookie perfectly round instead of stretched
ax.set_aspect("equal")
        
# Hide the axes, numbers, and grid lines
ax.axis("off")
        
# Display the completed cookie in the Streamlit app
st.pyplot(fig)


