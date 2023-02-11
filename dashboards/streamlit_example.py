import streamlit as st
import pandas as pd

## streamlit tutorial here

st.title("Welcome to my app")
# st.write("some words")

# '''Magic words'''

'''Look at my cute dog! :)'''

img = "https://github.com/emmaholt833/SeniorProject/blob/main/dashboards/data/ruby.jpg?raw=true"

# pic = "C:/Users/Emma/Documents/WI23/SeniorProject/SeniorProject_github/dashboards/data/ruby.jpg"
# pic2 = "/data/ruby.jpg"
st.image(img, width = 700)

name = st.text_input(label = "What is your name?")

st.write("Hello " + name + " how are you today?")


