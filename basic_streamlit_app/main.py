import streamlit as st
import pandas as pd

# Streamlit App
st.title("Basic Streamlit App")
st.write("This app demonstrates a simple interactive Streamlit application.")


# Display the dataframe
st.write("### Sample Data:")
st.dataframe(df)

# Interactive filtering example
column = st.selectbox("Select a column to filter:", df.columns)
unique_values = df[column].unique()
selected_value = st.selectbox(f"Select a value for {column}:", unique_values)

filtered_df = df[df[column] == selected_value]
st.write("### Filtered Data:")
st.dataframe(filtered_df)

