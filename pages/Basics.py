import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.header("Interactive widgets", anchor="interactive")

st.button("Click")
st.checkbox('Check')
st.radio('Pick', ['cats', 'dogs'])
size = st.select_slider('Pick a size', ['S', 'M', 'L'])
st.write("you picked " + {"S":"Small", "M":"Medium", "L": "Large"}[size])

st.file_uploader('Upload a CSV')
st.camera_input("Take a picture in streamlit")


st.header("Interactive plotting with matplotlib")

a = st.number_input("Enter a number", min_value=1, max_value=5, step=1, value=3)
b = st.slider("Another number", value=1, max_value=20)

color = st.color_picker('Line color')

st.latex(f"sin({a}x) x^{{" + str(b) + "}")

x = np.arange(0, 3, 0.1)
y = np.sin(a*x) * np.power(x, b)

fig = plt.figure()
plt.plot(x, y, color=color)

st.pyplot(fig)
