# 🧠 Custom Named Entity Recognition (NER) App using spaCy & Streamlit

## 🚀 Project Overview

This app allows users to explore Named Entity Recognition (NER) using their own **custom labels and patterns** through spaCy's powerful `EntityRuler` component. Built with Streamlit, the interface makes it simple to experiment with pattern-based NER in real-time.

Named Entity Recognition is the task of identifying entities like names, organizations, dates, etc., in text. With this app, you can take control by defining exactly which entities to detect — useful for industry-specific terms or domain-specific NLP tasks.

---

## 🛠 Setup Instructions

### 🔧 Requirements

- Python 3.7 or higher
- `spacy`
- `streamlit`

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/custom-ner-app.git
cd custom-ner-app

# Install dependencies
pip install -r requirements.txt

# Download the spaCy English model
python -m spacy download en_core_web_sm

# Run the Streamlit app
streamlit run app.py
```

## 🌐 Deployed Version
You can also try the app live here: [Live Demo]()

## 🎯 App Features
📥 Upload or input text directly into the app

🧩 Define custom entities using label-pattern dictionaries in JSON format

🧠 spaCy’s EntityRuler is used to apply your custom patterns

🎨 Highlighted visualization of entities using displacy

## 📝 Example Pattern Format
```bash
[
  { "label": "PRODUCT", "pattern": "iPhone" },
  { "label": "EVENT", "pattern": [{"LOWER": "world"}, {"LOWER": "cup"}] }
]
```
## 📷 Visual Example

## 📚 Useful Resources
- [spaCy Introduction](https://spacy.io/usage/spacy-101)
- [EntityRuler Guide](https://spacy.io/api/entityruler)
