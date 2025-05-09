import streamlit as st
import csv
import os

# CSV file path
csv_file = "user_ingredients.csv"

# Save new user ingredient to CSV
def save_user_ingredient_csv(name, data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["ingredient", "function", "safety", "allergens", "source", "environmental_impact"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "ingredient": name.lower(),
            "function": data["function"],
            "safety": data["safety"],
            "allergens": data["allergens"],
            "source": data["source"],
            "environmental_impact": data["environmental_impact"]
        })

# Load all user ingredients from CSV
def load_user_ingredients_csv():
    if not os.path.exists(csv_file):
        return {}
    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return {row["ingredient"]: {
            "function": row["function"],
            "safety": row["safety"],
            "allergens": row["allergens"],
            "source": row["source"],
            "environmental_impact": row["environmental_impact"]
        } for row in reader}

# Hardcoded ingredient database (you can extend it as needed)
ingredient_database = {
    "glycerin": {
        "function": "Humectant",
        "safety": "Safe",
        "allergens": "None",
        "source": "Plant-based",
        "environmental_impact": "Low"
    },
    "fragrance": {
        "function": "Scent",
        "safety": "Variable",
        "allergens": "Possible allergens",
        "source": "Synthetic",
        "environmental_impact": "High"
    },
    "water": {
        "function": "Solvent",
        "safety": "Safe",
        "allergens": "None",
        "source": "Natural",
        "environmental_impact": "Low"
    },
    "retinol": {
        "function": "Anti-aging",
        "safety": "Moderate",
        "allergens": "None",
        "source": "Synthetic",
        "environmental_impact": "Moderate"
    },
}

# Merge in user ingredients
user_ingredients = load_user_ingredients_csv()
ingredient_database.update(user_ingredients)

# Streamlit App
st.title("Makeup Ingredient Analyzer")
st.write("Enter ingredients separated by commas:")

user_input = st.text_input("Ingredients", "water, alcohol")

if user_input:
    ingredients = [i.strip().lower() for i in user_input.split(",")]

    for ing in ingredients:
        if ing in ingredient_database:
            st.subheader(f"{ing.title()}")
            st.write("Function:", ingredient_database[ing]["function"])
            st.write("Safety:", ingredient_database[ing]["safety"])
            st.write("Allergens:", ingredient_database[ing]["allergens"])
            st.write("Source:", ingredient_database[ing]["source"])
            st.write("Environmental Impact:", ingredient_database[ing]["environmental_impact"])
        else:
            st.warning(f"{ing.title()} not found in database.")
            with st.expander(f"Add details for {ing.title()}"):
                function = st.text_input(f"Function of {ing}", key=f"func_{ing}")
                safety = st.text_input(f"Safety info for {ing}", key=f"safety_{ing}")
                allergens = st.text_input(f"Allergens info for {ing}", key=f"allergens_{ing}")
                source = st.text_input(f"Source of {ing}", key=f"source_{ing}")
                env_impact = st.text_input(f"Environmental impact for {ing}", key=f"env_{ing}")
                
                if st.button(f"Save {ing.title()} info", key=f"save_{ing}"):
                    new_data = {
                        "function": function,
                        "safety": safety,
                        "allergens": allergens,
                        "source": source,
                        "environmental_impact": env_impact
                    }
                    save_user_ingredient_csv(ing, new_data)
                    st.success(f"Saved {ing.title()} to ingredient database. Please refresh to see updated info.")

# Footer
st.markdown("---")
st.caption("© 2025 Makeup Ingredient Analyzer – Built with ❤️ using Streamlit")
