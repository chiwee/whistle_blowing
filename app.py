import streamlit as st
st.image("header.jpg")
st.title("Dell Global Business Center Sdn Bhd")


st.date_input("Transaction Date")
st.radio("Your department:", ['AI','DS','QS','Logistic'])

st.camera_input("Case reported")