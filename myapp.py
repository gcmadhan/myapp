import streamlit as st
from PyDictionary import PyDictionary
from 

dic = PyDictionary()
st.balloons()


w = st.text_input("Enter the word here") 
m = dic.meaning(w)
for i in m:
    st.subheader(i)
    for j in m.get(i):
        st.write(j)

st.subheader("Synonums")
s=dic.synonym(w)
st.write(s)

st.subheader("Antonyms")
a = dic.antonym(w)
st.write(a)