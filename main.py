from pages.modules import *
import streamlit as st

import requests
import pandas as pd
import json

st.set_page_config(page_title="PLANTR | USING AI TO SAVE THE 🌎, ONE 🌱 AT A TIME", page_icon="🌿")

st.sidebar.page_link("main.py", label="HOME", icon="🏠")
st.sidebar.page_link("pages/scanPlant.py", label="SCAN A PLANT", icon="🌱")
st.sidebar.page_link("pages/follytest.py", label="PICK A LOCATION", icon="🗺️")
st.sidebar.page_link("pages/rippleEffects.py", label="PREDICT EFFECTS", icon="🌎")

st.image("images/notahomeplant(1).png")
st.header("", divider='green')
#Using AI to save the 🌎, one 🌱 at a time
st.header("**Drag in a picture of a plant and see how it could affect different ecosystems!**")
st.divider()
uploaded_file = st.file_uploader("Choose a file")


d = st.empty()
if uploaded_file is not None:
    image = uploaded_file.getvalue()
    st.image(image)
    
    d.success("**PROCESSING IMAGE...**")
    with open ('images/img.jpg','wb') as file:
        file.write(image)
    plantName = getPlant('images/img.jpg')
    st.header(f"{plantName[0]}: The {plantName[1]}", divider='green')
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
    st.header(f"About {plantName[0]}:", divider='green')
    pre_apiKey = "iZM0rbUN67u9PmtCMpaS0NyDY8gtXRNsKwK_-OIW-OE"

    url = f"https://trefle.io/api/v1/plants/search?token={pre_apiKey}&q={plantName[0]}"

    response = requests.get(url)
    plantSpecies = json.loads(response.text)['data'][0]['slug']
    plantDataURL = f"https://trefle.io/api/v1/species/{plantSpecies}?token={pre_apiKey}"
    response = requests.get(plantDataURL)
    plantData = json.loads(response.text)

    df = pd.DataFrame({
        "Native Locations": plantData['data']['distribution']['native']
        })
    df1 = pd.DataFrame({"Introduced to Locations": plantData['data']['distribution']['introduced']    
        })
    
    question = f"Q: Where does the plant species {plantName[0]} originate?"
    st.subheader("Q: Where does the plant originate?")    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    st.table(df)
    st.table(df)
    
    question = f"Q: What kind of climate does the plant species {plantName[0]} prefer?"
    st.subheader("Q: What kind of climate does the plant prefer?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What are the natural predators of the plant species {plantName[0]}?"
    st.subheader("Q: What are the natural predators of the plant?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What are the nutritional requirements of the plant species {plantName[0]}?"
    st.subheader("Q: What are the nutritional requirements of the plant?")
    st.write("Nutritional and growth data:")
    leff, rye = st.columns(2)
    with leff:
        st.write(plantData['data']['growth'])
    with rye:
        st.write(plantData['data']['specifications'])
    answer = askAI21(question+" \nA:")
    st.write(answer)
    st.header(f"About {plantName[0]}:", divider='green')
    
    question = f"Q: Where does the plant species {plantName[0]} originate?"
    st.subheader("Q: Where does the plant originate?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What kind of climate does the plant species {plantName[0]} prefer?"
    st.subheader("Q: What kind of climate does the plant prefer?")
    
    answer = askAI21(question+" \nA:")
    st.write(answer)
    
    question = f"Q: What are the natural predators of the plant species {plantName[0]}?"
    st.subheader("Q: What are the natural predators of the plant?")
    
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
st.header("why plantr?")
st.write("Agriculture is a very dominant part of Ethiopia's economy, just like how it is with most other developing countries. We have recently started to use a more modern and technology-based approach when it comes to farming; and this project aims to play a part in that.  \n  \nPlantr is a project that combines a chatGPT-like LLM (AI21) and an image recognition API (Pl@ntNet) to first recognize and identify plants from pictures and then give the user information about how the plant can be taken care of, how it could be used, etc.")
st.write("The main feature of this site is that you can use the LLM to roughly predict what kind of effect introducing a novel plant population would have on the ecosystem it joins. There's a map to choose co-ordinates and everything.  \n  \nThis approach is far from perfect, but I believe it paves the way towards using these AI models and API's in new and innovative ways.")
    
st.divider()
l, r = st.columns(2)
with r:
    st.caption("made with 💚 by Estifanos Tolemariam")
