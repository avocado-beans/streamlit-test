import streamlit as st
import streamlit_lottie

st.header("PLANTR is temporarily down for maintainance!", divider='green')
st.subheader("I'm modifying it until the day of the contest so it'll be down for a few days.")
st.write("Thanks for visiting the site, though! Trust me, this project will not disappoint :)")
st.write("I'm @tae2big on instagram if you want to contact me until then.")
st.divider()
st.image("images/farm.jpg")
st.divider()
st.header("Q: What is PLANTR?")
st.divider()
code = '''def plantr(_ecosystem):
    for _organism in _ecosystem():
        # check if organism is compatible with others
        for _other_organism in _ecosystem:
            if _compatible_:
                return WILL_CO_EXIST
            if not _compatible:
                # "co-species" to add to make the organisms co-operate 
                return _co_species(_organism, _other_organism).json()

    
def save_earth():
    # list of data about each organism in ecosystem
    eco_observations = []
    
    for _organism in ecosystem.analyze():
        # analyze organism
        org = _organism.analyze()
        # save to observation list
        org.plantr(eco_observations)
    
    # outcome
    return A_BETTER_EARTH'''
st.code(code)
st.caption("(This is pseudo-code to illustrate very loosely how this works.)")
st.write("Agriculture is a very dominant part of Ethiopia's economy, just like how it is with most other developing countries. We have recently started to use a more modern and technology-based approach when it comes to farming; and this project aims to play a part in that.  \n  \nPlantr is a project that combines a chatGPT-like LLM (AI21), an image recognition API (Pl@ntNet) and geo-spatial technology to first recognize and identify plants from pictures and then give the user information about how the plant can be taken care of, how it could be used, etc. And then it gives analysis on how the addition of that species to a novel ecosystem could affect said ecosystem.")

st.divider()
st.header("Q: Why?")
st.divider()
st.write("The goal is to make software that can be used not only to protect and save ecosystems, but to enhance them, make them stronger and more efficient. It's based on the (almost-baseless, I admit) assumption that nature doesn't need to be constantly bombarded with fertilizers or 'care and protection' procedures (such as terracing or drone-watering) in order to yield food long-term. ")
st.write("Ecosystems can fully sustain themselves while also providing abundant food, but only if the organisms that consitute them interact with each other in very specific ways. ")
st.write("By analyzing climate, geo-location and plant growth requirement data and using it to simulate how selected food crops and plants would interact with each other and their environment, we can manage our farms more efficiently while making them low-maintainance, and eliminate the need for invasive human action. Thus making food healthier, cheaper and basically saving the Earth in the process.")
st.write("_It's a long shot, but I think we can make it. Any support would help a lot._")
st.divider()
st.header("_that's_ the future we're headed for...")
st.image("images/lab.jpg")
left, right = st.columns(2)
with right:
  st.header("..._that's_ PLANTR.")
st.divider()
left, right = st.columns(2)
with right:
  st.caption("Made with (Platonic) Love, E. Tolemariam")
