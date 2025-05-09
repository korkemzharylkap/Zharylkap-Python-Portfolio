import streamlit as st
import pandas as pd
import json
import os
import re

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

# Paths to CSV files
MAIN_DB_PATH = 'StreamlitAppFinal/ingredients_database.csv'
USER_DB_PATH = 'StreamlitAppFinal/user_ingredients.csv'

# Function to load the main database
def load_main_database():
    if os.path.exists(MAIN_DB_PATH):
        df = pd.read_csv(MAIN_DB_PATH)
        return df
    else:
        st.error(f"Main database file '{MAIN_DB_PATH}' not found.")
        return None

# Function to load the user database
def load_user_database():
    if os.path.exists(USER_DB_PATH):
        df = pd.read_csv(USER_DB_PATH)
        return df
    else:
        st.error(f"User database file '{USER_DB_PATH}' not found.")
        return None

# Streamlit UI
st.title("💄 Makeup Ingredient Analyzer")
st.markdown("""
Analyze your makeup or skincare ingredient lists. Below are the contents of the ingredient databases.
""")

# Load and display the main database
st.subheader("Main Ingredient Database")
main_db = load_main_database()
if main_db is not None:
    st.write("First few rows of the dataset:", main_db.head())  # Display the first few rows of the main database

# Load and display the user database
st.subheader("User Ingredient Database")
user_db = load_user_database()
if user_db is not None:
    st.write("First few rows of the dataset:", user_db.head())  # Display the first few rows of the user database
