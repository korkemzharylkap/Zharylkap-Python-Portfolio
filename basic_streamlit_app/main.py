import streamlit as st
import pandas as pd

# Streamlit App
st.title("🐧 Penguins Data App")
st.write("This app demonstrates a simple interactive Streamlit application of Penguins Data Set.")

def load_data():
    df = pd.read_csv("data/penguins.csv")  # Using the existing penguins dataset
    return df

