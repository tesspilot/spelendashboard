import streamlit as st
import pandas as pd
from visualize_costs import create_playground_dashboard

# Set page config
st.set_page_config(
    page_title="Speelvoorzieningen Kosten Dashboard",
    page_icon="🎮",
    layout="wide"
)

# Use dark theme
st.markdown("""
    <style>
    .stApp {
        background-color: #1f1f1f;
        color: white;
    }
    .stDataFrame {
        background-color: #2f2f2f;
    }
    .stMarkdown {
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Add title and description
st.title("🎮 Speelvoorzieningen Kosten Dashboard")
st.markdown("""
Dit dashboard geeft een overzicht van de kosten en onderhoud van speelvoorzieningen.
Het visualiseert verschillende aspecten zoals:
- Aantal voorzieningen per type
- Inspectiekosten verdeling
- Storingskosten vs levensduur
- Periodiek onderhoudskosten
- Groot onderhoud prognose
- Exploitatiebudget analyse
""")

# Load and cache the data
@st.cache_data
def load_data():
    return pd.read_csv('playground_costs.csv')

# Load the data
df = load_data()

# Create tabs for different views
tab1, tab2 = st.tabs(["📊 Dashboard", "📋 Data"])

with tab1:
    # Display the dashboard
    st.plotly_chart(create_playground_dashboard(df), use_container_width=True)
    
with tab2:
    # Display the raw data with filters
    st.subheader("Ruwe Data")
    
    # Add filters
    selected_assets = st.multiselect(
        "Filter op Asset Type",
        options=df['Asset'].unique(),
        default=df['Asset'].unique()
    )
    
    # Filter the dataframe
    filtered_df = df[df['Asset'].isin(selected_assets)]
    
    # Display the filtered dataframe
    st.dataframe(filtered_df, use_container_width=True)
    
    # Add download button
    st.download_button(
        label="Download Data als CSV",
        data=filtered_df.to_csv(index=False).encode('utf-8'),
        file_name='speelvoorzieningen_kosten.csv',
        mime='text/csv'
    )

# Add footer
st.markdown("---")
st.markdown("Dashboard gemaakt met Streamlit en Plotly")
