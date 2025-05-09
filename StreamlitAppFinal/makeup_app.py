import streamlit as st
import pandas as pd
import json
import os
import re
import urllib.request
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

# File paths

url = "https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/refs/heads/main/StreamlitAppFinal/ingredient_database.json"

# Send GET request to fetch the raw JSON data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    print(data)  # Print the parsed JSON data
else:
    print(f"Failed to fetch the file: {response.status_code}")
