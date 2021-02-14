import streamlit as st
x_value = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is updated now', x_value * x_value)
