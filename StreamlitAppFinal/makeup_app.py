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
main_url = "https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/ingredient_database.json"
user_url = "https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/user_ingredients.json"

main_resp = requests.get(main_url)
MAIN_DB_FILE = json.loads(main_resp.text)
print(MAIN_DB_FILE)

user_resp = requests.get(user_url)
USER_DB_FILE = json.loads(user_resp.text)
print(USER_DB_FILE)
    
