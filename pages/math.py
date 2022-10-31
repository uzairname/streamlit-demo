import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Interactive plotting with matplotlib")

a = st.number_input("Enter a number", min_value=1, max_value=5, step=1, value=3)
b = st.slider("Another number", value=1, max_value=20)

st.latex(f"sin({a}x) x^{{" + str(b) + "}")

x = np.arange(0, 3, 0.1)
y = np.sin(a*x) * np.power(x, b)

fig = plt.figure()
plt.plot(x, y)

st.pyplot(fig)
