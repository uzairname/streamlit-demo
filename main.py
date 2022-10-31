import streamlit as st

st.title("tita")

st.header("Math")

a = st.number_input("Enter a number", min_value=0, max_value=100, step=1)
b = st.slider("Another number")

st.latex(f"{a} x^{{" + str(b) + "}")



