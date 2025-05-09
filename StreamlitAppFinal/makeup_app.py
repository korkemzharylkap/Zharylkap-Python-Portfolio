import streamlit as st
import pandas as pd
import json
import os
import re

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

df = 'StreamlitAppFinal/ingredients_database.csv'
USER_DB_PATH = 'StreamlitAppFinal/user_ingredients.csv'


st.write("First few rows of the dataset:", df.head())
