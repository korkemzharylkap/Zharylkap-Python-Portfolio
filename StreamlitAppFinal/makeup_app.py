import streamlit as st
import pandas as pd
import json
import os
import re
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

# Functions to load ingredients from remote URLs
def load_user_ingredients_from_url(url="https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/user_ingredients.json"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching user ingredients: {e}")
        return {}

def load_user_ingredients_database_from_url(url="https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/ingredient_database.json"):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching ingredients database: {e}")
        return {}

# Load main ingredient database
def load_main_database():
    return load_user_ingredients_database_from_url()

# Load user-provided ingredient data
def load_user_database():
    return load_user_ingredients_from_url()

# Merge main and user databases
def get_combined_database():
    main_db = load_main_database()
    user_db = load_user_database()
    combined_db = {**main_db, **user_db}
    return combined_db

# Analyze ingredients function
def analyze_ingredients(raw_input):
    database = get_combined_database()
    parsed = parse_ingredients(raw_input)
    results = []
    unknowns = []
    for ing in parsed:
        ing_lc = ing.lower()
        info = database.get(ing_lc)
        if info:
            results.append({
                "Ingredient": ing,
                "Function": info.get("function", "N/A"),
                "Safety": info.get("safety", "N/A"),
                "Allergens": info.get("allergens", "N/A"),
                "Source": info.get("source", "N/A"),
                "Environmental Impact": info.get("environmental_impact", "N/A")
            })
        else:
            unknowns.append(ing)
    return results, unknowns

# Streamlit UI setup
st.title("💄 Makeup Ingredient Analyzer")
st.markdown("""
Analyze your makeup or skincare ingredient lists. Paste your ingredients or upload a `.txt` file to learn about each item's purpose, safety, and impact.
""")

# Input methods for uploading a file or pasting ingredients
uploaded_file = st.file_uploader("Upload a text file with ingredients (comma-separated or one per line)", type=["txt"])
text_input = st.text_area("Or paste your ingredient list here", height=200)

# Process input
results_df = None
unknown_ingredients = []

if uploaded_file is not None:
    try:
        content = uploaded_file.read().decode("utf-8")
        results, unknowns = analyze_ingredients(content)
        results_df = pd.DataFrame(results)
        unknown_ingredients = unknowns
    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")
elif text_input.strip():
    results, unknowns = analyze_ingredients(text_input)
    results_df = pd.DataFrame(results)
    unknown_ingredients = unknowns

# Display results
if results_df is not None:
    st.success(f"✅ Analyzed {len(results_df)} ingredient(s).")
    st.dataframe(results_df, use_container_width=True)
    st.download_button(
        label="📥 Download Results as CSV",
        data=results_df.to_csv(index=False),
        file_name="ingredient_analysis_results.csv",
        mime="text/csv"
    )

# Add new ingredients
if unknown_ingredients:
    st.subheader("🔧 Add New Ingredients")
    for ing in unknown_ingredients:
        with st.expander(f"Add details for: {ing}"):
            function = st.text_input(f"Function of {ing}", key=f"func_{ing}")
            safety = st.text_input(f"Safety of {ing}", key=f"safety_{ing}")
            allergens = st.text_input(f"Allergens in {ing}", key=f"allergens_{ing}")
            source = st.text_input(f"Source of {ing}", key=f"source_{ing}")
            environmental_impact = st.text_input(f"Environmental Impact of {ing}", key=f"impact_{ing}")
            if st.button(f"Save {ing}", key=f"save_{ing}"):
                new_data = {
                    "function": function or "N/A",
                    "safety": safety or "Unknown",
                    "allergens": allergens or "Unknown",
                    "source": source or "Unknown",
                    "environmental_impact": environmental_impact or "Unknown"
                }
                save_user_ingredient(ing, new_data)
                st.success(f"Saved data for '{ing}'.")
                st.rerun()

# Footer
st.markdown("---")
st.caption("© 2025 Makeup Ingredient Analyzer – Built with ❤️ using Streamlit")
