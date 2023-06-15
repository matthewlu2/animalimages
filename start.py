import streamlit as st
from PIL import Image


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/animaldata/main/'


option = st.selectbox(
    'Please select what animal you want to see!',
    ('Cat', 'Dog', 'Rabbit'))

option1 = option.lower()

img = f'{IMG_REPO}/{option1}.jpg'
st.image(img)