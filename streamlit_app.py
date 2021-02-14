import streamlit as st
x_value = st.slider('x')  # 👈 this is a widget
my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.
st.write(x_value, 'squared is updated now', x_value * x_value)

