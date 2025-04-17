import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
import json

# Title and instructions
st.title("🔍 Custom Named Entity Recognition (NER) with spaCy")
st.markdown("""
This app lets you explore Named Entity Recognition with your own custom labels and patterns using spaCy's **EntityRuler**.

- 📥 Input or upload text
- 🧠 Add your own entity patterns
- 🎯 See detected entities highlighted
""")

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# --- Sidebar: Custom Patterns ---
st.sidebar.header("🧩 Define Custom Entity Patterns")
custom_patterns_input = st.sidebar.text_area(
    "Enter custom patterns in JSON (list of dicts with 'label' and 'pattern'):",
    value='''[
  {"label": "PRODUCT", "pattern": "iPhone"},
  {"label": "EVENT", "pattern": [{"LOWER": "world"}, {"LOWER": "cup"}]}
]''',
    height=200
)

# --- Text Input or File Upload ---
st.subheader("📄 Text Input")
text_source = st.radio("Choose input method:", ["Type/Paste Text", "Upload .txt File"])

text = ""
if text_source == "Type/Paste Text":
    text = st.text_area("Enter your text here:", height=200)
else:
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded_file:
        text = uploaded_file.read().decode("utf-8")

# --- Process Text with Custom Patterns ---
if text:
    try:
        custom_patterns = json.loads(custom_patterns_input)

        # Remove existing custom_ruler if needed
        if "custom_ruler" in nlp.pipe_names:
            nlp.remove_pipe("custom_ruler")

        # Add custom EntityRuler
        ruler = nlp.add_pipe("entity_ruler", name="custom_ruler", before="ner", config={"overwrite_ents": True})
        ruler.add_patterns(custom_patterns)

        # Run NLP pipeline
        doc = nlp(text)

        # Visualize entities
        st.subheader("🔎 Recognized Entities")
        html = displacy.render(doc, style="ent", minify=True, jupyter=False)
        st.write(html, unsafe_allow_html=True)

        # Display entities in table
        st.subheader("🗂️ Entity Details")
        if doc.ents:
            entity_data = [{"Text": ent.text, "Label": ent.label_} for ent in doc.ents]
            st.table(entity_data)
        else:
            st.info("No entities found.")

    except json.JSONDecodeError:
        st.error("❌ Error: Invalid JSON in custom patterns.")
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
else:
    st.info("Please enter or upload text to analyze.")
