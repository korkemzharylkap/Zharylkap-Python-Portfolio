import streamlit as st
import pandas as pd
import json
import os
import re
import urllib.request

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

# File paths
main_url = "https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/ingredient_database.json"
user_url = "https://raw.githubusercontent.com/korkemzharylkap/Zharylkap-Python-Portfolio/main/StreamlitAppFinal/user_ingredients.json"

# Load the main ingredient database from the raw URL
with urllib.request.urlopen(main_url) as response:
    MAIN_DB_FILE = json.load(response)

# Load the user ingredient database from the raw URL
with urllib.request.urlopen(user_url) as response:
    USER_DB_FILE = json.load(response)
    
# Load main ingredient database
def load_main_database():
    return {k.lower(): v for k, v in MAIN_DB_FILE.items()}

# Load user-provided ingredient data
def load_user_database():
    return {k.lower(): v for k, v in USER_DB_FILE.items()}


# Save new ingredient to user database
def save_user_ingredient(name, data):
    name = name.strip().lower()
    user_db = load_user_database()
    user_db[name] = data
    with open(USER_DB_FILE, "w", encoding="utf-8") as f:
        json.dump(user_db, f, indent=4)

# Merge main and user databases
def get_combined_database():
    main_db = load_main_database()
    user_db = load_user_database()
    combined_db = {**main_db, **user_db}
    return combined_db
    
# Parse and clean ingredient input
def parse_ingredients(raw_text):
    split_items = re.split(r',|;|\n', raw_text)
    return [item.strip() for item in split_items if item.strip()]

# Analyze ingredients
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

# Streamlit UI
st.title("💄 Makeup Ingredient Analyzer")
st.markdown("""
Analyze your makeup or skincare ingredient lists. Paste your ingredients or upload a `.txt` file to learn about each item's purpose, safety, and impact.
""")

# Input methods
st.subheader("📥 Input Ingredients")
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

# Sample ingridients
with st.expander("🧪 Sample Ingredients"):  # Corrected here
    if st.button("Load Sample Data"):
        sample_ingredients = "Glycerin, Fragrance, Phenoxyethanol, Water, Retinol"
        df_sample = pd.DataFrame(analyze_ingredients(sample_ingredients)[0])

        st.dataframe(df_sample, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 Makeup Ingredient Analyzer – Built with ❤️ using Streamlit")
