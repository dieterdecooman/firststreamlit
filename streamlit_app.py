import streamlit as st
x_value = st.slider('x')  # 👈 this is a widget
my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

st.write(x_value, 'squared is updated now', x_value * x_value)
tel = [['jake',4098]['sape',4139]]
tel
st.write(tel)
#st.bar_chart(data=tel, width=0, height=0, use_container_width=True)
