import streamlit as st
from pages.modules import *
from streamlit_back_camera_input import back_camera_input

st.set_page_config(page_title="PLANTR | SCAN A PLANT", page_icon="🌿")


st.sidebar.page_link("main.py", label="HOME", icon="🏠")
st.sidebar.page_link("pages/scanPlant.py", label="SCAN A PLANT", icon="🌱")
st.sidebar.page_link("pages/follytest.py", label="PICK A LOCATION", icon="🗺️")
st.sidebar.page_link("pages/rippleEffects.py", label="PREDICT EFFECTS", icon="🌎")

st.header("scan that plant: tap the camera!", divider='green')
image = back_camera_input()
d = st.empty()
c = st.empty()
c.subheader("**Snap a pic' of the 🪴 you want to analyze! Get to a decent distance from the plant (ideally 50 to 100cm ) and tap the window below to take the shot! (Try to make sure the plant is isolated from other plants and that you capture a unique part of it to ensure there is no confusion on the AI's end.)**")


if image:
    c.image(image)
    
    d.success("**PROCESSING IMAGE...**")
    #with open ('img.jpg','wb') as file:
        #file.write(image.getbuffer())
    plantName = getPlant('images/img.jpg')
    c.header(f"{plantName[0]}: The {plantName[1]}", divider='green')
    d.success("**DONE!**")
    left, right = st.columns(2)
    with open ('plntNM.txt','w') as file:
        file.write(plantName[0])
    with open ('cmnNM.txt', 'w') as file:
        file.write("The ")
        file.write(plantName[1])
    response = askAI21("Q: Tell me about the plant species known as "+plantName[0]+". \nA:")
    with left:
        st.write(response)
        st.write("**(Hint: Go to the sidebar and hit PICK LOCATION to pick the area you wanna see this plant placed.)**")
    with right:
        st.image("images/img.jpg")
    st.divider()
    
    st.header(f"About {plantName[0]}:")
    
    question = f"Q: Where does the plant species {plantName[0]} originate?"
    st.subheader("Q: Where does the plant originate?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What kind of climate does the plant species {plantName[0]} prefer?"
    st.subheader("Q: What kind of climate does the plant prefer?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What are the natural predators of the plant species {plantName[0]}?"
    st.subheader("What are the natural predators of the plant?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What are the nutritional requirements of the plant species {plantName[0]}?"
    st.subheader("Q: What are the nutritional requirements of the plant?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: How can the plant species {plantName[0]} be used for human benefit?"
    st.subheader("Q: How can I use this plant?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: If edible, what kind of food can I make with the plant species {plantName[0]}?"
    st.subheader("Q: What kind of food can I make with it? (if possible)")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
st.divider()
l, r = st.columns(2)
with r:
    st.caption("made with ❤️ by Estifanos Tolemariam")

    

