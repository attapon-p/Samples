import streamlit as st

st.title("Upload to Cloud!")
name = st.text_input("Enter name:")
b = st.button("Click Me")
if b:
    st.write(name)