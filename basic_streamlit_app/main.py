import streamlit as st
import pandas as pd

# Streamlit App
st.title("🐧 Penguins Data App")
st.write("This app demonstrates a simple interactive Streamlit application of Penguins Data Set.")

def load_data():
    df = pd.read_csv("data/penguins.csv")  # Using the existing penguins dataset
    return df

# Dropdown to select species
species = st.selectbox(
    "Select Species:",
    options=data['species'].unique()
)

# Dropdown to select island
island = st.selectbox(
    "Select Island:",
    options=data['island'].unique()
)

# Slider for bill length
bill_length = st.slider(
    "Bill Length (mm):",
    min_value=int(data['bill_length_mm'].min()),
    max_value=int(data['bill_length_mm'].max()),
    step=0.1,
    value=(data['bill_length_mm'].min(), data['bill_length_mm'].max())
)

# Slider for bill depth
bill_depth = st.slider(
    "Bill Depth (mm):",
    min_value=int(data['bill_depth_mm'].min()),
    max_value=int(data['bill_depth_mm'].max()),
    step=0.1,
    value=(data['bill_depth_mm'].min(), data['bill_depth_mm'].max())
)

# Slider for flipper length
flipper_length = st.slider(
    "Flipper Length (mm):",
    min_value=int(data['flipper_length_mm'].min()),
    max_value=int(data['flipper_length_mm'].max()),
    step=1,
    value=(data['flipper_length_mm'].min(), data['flipper_length_mm'].max())
)

# Slider for body mass
body_mass = st.slider(
    "Body Mass (g):",
    min_value=int(data['body_mass_g'].min()),
    max_value=int(data['body_mass_g'].max()),
    step=10,
    value=(data['body_mass_g'].min(), data['body_mass_g'].max())
)

# Filter the dataset based on user input
filtered_data = data[
    (data['species'] == species) &
    (data['island'] == island) &
    (data['bill_length_mm'] >= bill_length[0]) & (data['bill_length_mm'] <= bill_length[1]) &
    (data['bill_depth_mm'] >= bill_depth[0]) & (data['bill_depth_mm'] <= bill_depth[1]) &
    (data['flipper_length_mm'] >= flipper_length[0]) & (data['flipper_length_mm'] <= flipper_length[1]) &
    (data['body_mass_g'] >= body_mass[0]) & (data['body_mass_g'] <= body_mass[1])
]

# Display filtered data
st.write("Filtered Penguin Data", filtered_data)

# Display a sample plot for visualizing relationships (optional)
st.subheader("Bill Length vs. Bill Depth")
st.scatter_chart(filtered_data[['bill_length_mm', 'bill_depth_mm']])
