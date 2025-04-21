import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quadratic Function Plotter", layout="centered")

# Title
st.title("Quadratic Function Plotter")

st.markdown("Adjust the sliders to modify the quadratic function:")

# --- Slider Inputs ---
a = st.slider("Coefficient a", min_value=-5.0, max_value=5.0, value=1.0, step=0.1)
b = st.slider("Coefficient b", min_value=-10.0, max_value=10.0, value=2.0, step=0.1)
c = st.slider("Coefficient c", min_value=-20.0, max_value=20.0, value=3.0, step=0.1)

# --- Display LaTeX formula ---
st.latex(f"y = {a}x^2 + {b}x + {c}")

# --- Plot ---
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

fig, ax = plt.subplots()
ax.plot(x, y, label=fr"$y = {a}x^2 + {b}x + {c}$", color="blue")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Graph of the Quadratic Function")
ax.grid(True)
ax.legend()

st.pyplot(fig)
