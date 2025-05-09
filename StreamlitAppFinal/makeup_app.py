import streamlit as st
import pandas as pd
import json
import os
import re


# Safety dropdown with custom input
SAFETY_OPTIONS = ["Safe", "Moderate", "Low Risk", "High Risk", "Toxic", "Unknown", "Other"]
IMPACT_OPTIONS = ["Low", "Moderate", "High", "Unknown", "Other"]

# Set Streamlit page configuration
st.set_page_config(page_title="💄 Makeup Ingredient Analyzer", layout="centered")

# File paths
MAIN_DB_FILE = "StreamlitAppFinal/ingredient_database.json"
USER_DB_FILE = "StreamlitAppFinal/user_ingredients.json"

# Load main ingredient database
def load_main_database():
    if os.path.exists(MAIN_DB_FILE):
        with open(MAIN_DB_FILE, "r", encoding="utf-8") as f:
            return {k.lower(): v for k, v in json.load(f).items()}
    else:
        st.error(f"Main database file '{MAIN_DB_FILE}' not found.")
        return {}

# Load user-provided ingredient data
def load_user_database():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r", encoding="utf-8") as f:
            return {k.lower(): v for k, v in json.load(f).items()}
    else:
        return {}

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

# Dropdown-based unknown ingredient entry
if unknown_ingredients:
    st.subheader("🔧 Add a New Ingredient")
    selected_unknown = st.selectbox("Select an unknown ingredient to add details", unknown_ingredients, key="unknown_selector")
    
    if selected_unknown:
        function = st.text_input(f"Function of {selected_unknown}", key=f"func_{selected_unknown}")

        # Safety dropdown with custom input
        safety_choice = st.selectbox(f"Safety of {selected_unknown}", SAFETY_OPTIONS, key=f"safety_choice_{selected_unknown}")
        safety = st.text_input("Enter custom safety description", key=f"safety_custom_{selected_unknown}") 
        if safety_choice == "Other" 
        else safety_choice

        allergens = st.text_input(f"Allergens in {selected_unknown}", key=f"allergens_{selected_unknown}")
        source = st.text_input(f"Source of {selected_unknown}", key=f"source_{selected_unknown}")

        # Environmental Impact dropdown with custom input
        impact_choice = st.selectbox(f"Environmental Impact of {selected_unknown}", IMPACT_OPTIONS, key=f"impact_choice_{selected_unknown}")
        environmental_impact = st.text_input("Enter custom impact description", key=f"impact_custom_{selected_unknown}")
        if impact_choice == "Other" 
        else impact_choice

                
            if st.button(f"Save {selected_unknown}", key=f"save_{selected_unknown}"):
            new_data = {
                "function": function or "N/A",
                "safety": safety or "Unknown",
                "allergens": allergens or "Unknown",
                "source": source or "Unknown",
                "environmental_impact": environmental_impact or "Unknown"
            }
            save_user_ingredient(selected_unknown, new_data)
            st.success(f"Saved data for '{selected_unknown}'.")
            st.rerun()
                
# Sample ingredients
with st.expander("🧪 Sample Ingredients"):
    if st.button("Load Sample Data"):
        sample_ingredients = "Glycerin, Fragrance, Phenoxyethanol, Water, Retinol"
        sample_results, _ = analyze_ingredients(sample_ingredients)
        df_sample = pd.DataFrame(sample_results)
        st.dataframe(df_sample, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2025 Makeup Ingredient Analyzer – Built with ❤️ using Streamlit")
