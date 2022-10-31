import streamlit as st
from keybert import KeyBERT
from transformers.models import roberta


def load_model():
    return KeyBERT(model=roberta)


kw_model = load_model()


st.title("Keywords From a Paragraph")
doc = st.text_input(label="Enter a paragraph, to see its keywords")


keywords = kw_model.extract_keywords(doc)

st.write(keywords)

