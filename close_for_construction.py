import streamlit as st
import streamlit_lottie

st.title("Super sorry, dude! :green[Plantr] is temporarily down for :green[maintainance] and :green[development!]")
st.lottie("https://lottie.host/84c0c93b-2d47-4441-8a72-3802742681df/2MjzLbcImk.json")
st.divider()
st.subheader("**I'm modifying it until the day of the contest so it'll be down for a few days.**")
st.subheader("**Thanks for visiting the site, though! Trust me, this project will not disappoint :)**")
st.subheader("**I'm [@tae2big](https://www.instagram.com/tae2big/) on instagram and [@avocado-beans](https://github.com/avocado-beans) on github if you want to contact me for some reason.**")
st.divider()
st.header("Q: But until then, _what is :green[plantr?]_")
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
st.caption("**(The about is pseudo-code for decoration purposes. It's not supposed to make sense.)**")
st.write(":green[**Agriculture**] **is a very dominant part of Ethiopia's economy, just like how it is with most other developing countries. We have recently started to use a more modern and technology-based approach when it comes to farming; and this project aims to play a part in that.**")
st.write(":green[**Plantr**] **is a project that combines a chatGPT-like LLM (AI21), an image recognition API (Pl@ntNet) and geo-spatial technology to first recognize and identify plants from pictures and then give the user information about how the plant can be taken care of, how it could be used, etc. And then it gives analysis on how the addition of that species to a novel ecosystem could affect said ecosystem.**")

st.divider()
st.header("_Q: Why :green[plantr?]_")
st.divider()
st.write("**If you're talking about the name, I genuinely have no clue. It was a placeholder at first but then it just stuck, I guess. Like, c'mon, it's not _that_ bad.**")
st.write("**But the goal is to make software that can be used not only to protect and save ecosystems, but to :green[**enhance**] them, make them :green[**stronger**] and more :green[**efficient.**] It's based on the (almost-baseless, I admit) assumption that nature doesn't need to be constantly bombarded with fertilizers or 'care and protection' procedures (such as terracing or drone-watering) in order to yield food long-term.**")
st.write(":green[**Ecosystems can fully sustain themselves**] **while also providing abundant food, but only if the organisms that consitute them** :green[**interact with each other in very specific ways.**]")
st.write("**By analyzing climate, geo-location and plant growth requirement data and using it to :green[**simulate**] how selected food crops and plants would interact with each other and their environment, we can manage our farms more efficiently while making them low-maintainance, and :green[**eliminate the need for invasive human action.**] Thus making food :green[**healthier, cheaper**] and basically :green[**saving the Earth**] in the process.**")
st.write("**:green[_It's a long shot, but I think we can make it. Any support would help a lot._]**")
st.divider()
st.header("_that's the future we're headed for..._")
st.divider()
st.image("images/lab.jpg")
left, right = st.columns(2)
st.divider()
with right:
  st.header("..._that's_ :green[_plantr._]")
st.divider()
left, right = st.columns(2)
with right:
  st.caption("**Made with (Platonic) Love, E. Tolemariam**")
