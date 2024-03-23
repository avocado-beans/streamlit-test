import streamlit as st
from modules import *
from streamlit_bcp import back_camera_input

image = back_camera_input()
if image:
    st.image(image)
    with open ('img.jpg','wb') as file:
          file.write(image.getbuffer())

