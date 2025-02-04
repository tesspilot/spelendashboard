import streamlit as st
import pandas as pd
from visualize_costs import create_playground_dashboard

# Set page config
st.set_page_config(
    page_title="Speelvoorzieningen Kosten Dashboard",
    page_icon="🎮",
    layout="wide"
)

# Add title
st.title("Speelvoorzieningen Kosten Dashboard")

# Read and process data
df = pd.read_csv('playground_costs.csv')

# Create figure
fig = create_playground_dashboard(df)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Add footer
st.markdown("---")
st.markdown("Dashboard gemaakt met Streamlit en Plotly")
