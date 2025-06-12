# energy_app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and encoders
model = joblib.load('total_renewable_model.pkl')
sector_encoder = joblib.load('sector_encoder.pkl')
energy_sources = [
    'Hydroelectric Power', 'Geothermal Energy', 'Solar Energy',
    'Wind Energy', 'Wood Energy', 'Waste Energy', 'Fuel Ethanol, Excluding Denaturant',
    'Biomass Losses and Co-products', 'Biomass Energy', 'Renewable Diesel Fuel',
    'Other Biofuels', 'Biodiesel'
]

st.title("🔋 Renewable Energy Forecast Explorer")

selected_source = st.selectbox("Select Energy Source", energy_sources)

selected_year = st.slider("Select Year", min_value=2024, max_value=2050, value=2030)

# Mock-up prediction (replace with real model later)
st.subheader(f" Predicted Usage of {selected_source} in {selected_year}")
st.metric(label="Estimated TWh", value=f"{np.random.uniform(20, 300):.2f} TWh")

# Show sector dominance forecast
st.subheader(f"📊 Predicted Sector Distribution for {selected_source}")
sector_predictions = {
    'Residential': np.random.uniform(10, 30),
    'Commercial': np.random.uniform(5, 25),
    'Industrial': np.random.uniform(20, 50),
    'Electric Power': np.random.uniform(50, 100),
    'Transportation': np.random.uniform(2, 15),
}
sector_df = pd.DataFrame(list(sector_predictions.items()), columns=['Sector', 'Usage (TWh)'])
st.bar_chart(sector_df.set_index('Sector'))