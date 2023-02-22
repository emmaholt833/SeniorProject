import streamlit as st
import pandas as pd

st.title("My awesome app")

st.write("Add some text")

'''magic text'''

name = st.text_input(label = "What is your name?")

st.write("Hello " + name + " how are you?")

img = "https://github.com/emmaholt833/SeniorProject/blob/main/dashboards/data/ruby.jpg?raw=true"

st.image(img)

st.snow()


