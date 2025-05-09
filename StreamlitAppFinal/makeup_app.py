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

# Specify the path to your JSON file
file_path = 'ingredient_database.json'

# Open the JSON file and load its contents
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Print the data to check what has been loaded
print(data)
