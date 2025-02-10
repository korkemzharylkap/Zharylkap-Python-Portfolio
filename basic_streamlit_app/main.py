import streamlit as st
import pandas as pd

# Streamlit App
st.title("🐧 Penguins Data App")
st.write("This app demonstrates a simple interactive Streamlit application of Penguins Data Set.")

df = pd.read_csv('basic_streamlit_app/data/penguins.csv')

#Dropdown to select species
species = st.selectbox(
    "Select Species:",
    options=df['species'].unique() if 'species' in df.columns else []
)
# Dropdown to select island
island = st.selectbox(
    "Select Island:",
    options=df['island'].unique() if 'island' in df.columns else []
)
# Slider for bill length (ensure all values are floats)
bill_length = st.slider(
    "Bill Length (mm):",
    min_value=float(df['bill_length_mm'].min()) if 'bill_length_mm' in df.columns else 0.0,
    max_value=float(df['bill_length_mm'].max()) if 'bill_length_mm' in df.columns else 100.0,
    step=0.1,
    value=(float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max())) if 'bill_length_mm' in df.columns else (0.0, 100.0)
)
# Slider for bill depth (ensure all values are floats)
bill_depth = st.slider(
    "Bill Depth (mm):",
    min_value=float(df['bill_depth_mm'].min()) if 'bill_depth_mm' in df.columns else 0.0,
    max_value=float(df['bill_depth_mm'].max()) if 'bill_depth_mm' in df.columns else 100.0,
    step=0.1,
    value=(float(df['bill_depth_mm'].min()), float(df['bill_depth_mm'].max())) if 'bill_depth_mm' in df.columns else (0.0, 100.0)
)
# Slider for flipper length (ensure all values are integers)
flipper_length = st.slider(
    "Flipper Length (mm):",
    min_value=int(df['flipper_length_mm'].min()) if 'flipper_length_mm' in df.columns else 0,
    max_value=int(df['flipper_length_mm'].max()) if 'flipper_length_mm' in df.columns else 100,
    step=1,
    value=(int(df['flipper_length_mm'].min()), int(df['flipper_length_mm'].max())) if 'flipper_length_mm' in df.columns else (0, 100)
)

# Slider for body mass (ensure all values are integers)
body_mass = st.slider(
    "Body Mass (g):",
    min_value=int(df['body_mass_g'].min()) if 'body_mass_g' in df.columns else 0,
    max_value=int(df['body_mass_g'].max()) if 'body_mass_g' in df.columns else 10000,
    step=10,
    value=(int(df
    ['body_mass_g'].min()), int(df['body_mass_g'].max())) if 'body_mass_g' in df.columns else (0, 10000)
)
# Filter the dataset based on user input
filtered_data = df[
    (df['species'] == species) &
    (df['island'] == island) &
    (df['bill_length_mm'] >= bill_length[0]) & (df['bill_length_mm'] <= bill_length[1]) &
    (df['bill_depth_mm'] >= bill_depth[0]) & (df['bill_depth_mm'] <= bill_depth[1]) &
    (df['flipper_length_mm'] >= flipper_length[0]) & (df['flipper_length_mm'] <= flipper_length[1]) &
    (df['body_mass_g'] >= body_mass[0]) & (df['body_mass_g'] <= body_mass[1])
]
st.write("Filtered Penguin Data", filtered_data)

# Display a sample plot for visualizing relationships (optional)
st.subheader("Bill Length vs. Bill Depth")
st.scatter_chart(filtered_data[['bill_length_mm', 'bill_depth_mm']])
