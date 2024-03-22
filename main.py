import streamlit as st
from modules import *

picture = st.camera_input("Take a picture")

if picture:
    with open ('img.jpg','wb') as file:
          file.write(picture.getbuffer())

    plantName = getPlant('img.jpg')
    st.header(plantName)
