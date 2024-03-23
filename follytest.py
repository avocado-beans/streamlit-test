import folium
import streamlit as st

from streamlit_folium import st_folium

st.set_page_config(
    page_title="streamlit-folium documentation",
    page_icon=":world_map:️",
    layout="wide",
)


left, right = st.columns(2)


with left:
    """
    If we take a look at the example from the Home page, it might seem trivial. We
    define a single point with a marker and pop-up and display it:
    """
    with st.echo():
        

        # center on Liberty Bell, add marker
        m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
        ).add_to(m)

        # call to render Folium map in Streamlit
        st_data = st_folium(m, width=725)

with right:
    """
    But behind the scenes, a lot more is happening _by default_. The return value of
    `st_folium` is set to `st_data`, and within this Python variable is information
    about what is being displayed on the screen:
    """

    st_data

    """
    As the user interacts with the data visualization, the values for `bounds` are
    constantly updating, along with `zoom`. With these values available in Python, we
    can now limit queries based on bounding box, change the marker size based on the
    `zoom` value and much more!
    """

