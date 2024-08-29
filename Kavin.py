import streamlit as st

st.set_page_config("K logo.png")

st.write ("Hello World, this is my website where you can do nothing exept read the text you are reading wite now and take a photo.")
st.caption("Made from Kavin.D")
st.file_uploader("Upload A File")
st.color_picker("")
st.checkbox("")
Admin_Check = st.chat_input("Enter Admin Code")
st.code('print ("Hello world")')
if Admin_Check == "redbell1234":
    camera = False