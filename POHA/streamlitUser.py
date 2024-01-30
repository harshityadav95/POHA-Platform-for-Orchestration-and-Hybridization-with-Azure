import streamlit as st
from streamlit_js_eval import js_eval

st.title("Get client info")

width, height = js_eval("window.innerWidth", "window.innerHeight")

st.write(f"The window width is {width} pixels")
st.write(f"The window height is {height} pixels")
