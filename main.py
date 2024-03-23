import streamlit as st
import folium
from streamlit_folium import st_folium
from modules import *
from ai import askAI21
from streamlit_back_camera_input import back_camera_input

image = back_camera_input()
if image:
    st.image(image)
    with open ('img.jpg','wb') as file:
          file.write(image.getbuffer())
    plantName = getPlant('img.jpg')
    st.header(plantName)
    response = askAI21("Q: Tell me about the plant species known as "+plantName+". \nA:")
    st.subheader(response)
    
    

