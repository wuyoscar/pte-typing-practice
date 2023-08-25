from pte_formatter import OConverter
import streamlit as st

# Initialize session state
if 'url' not in st.session_state:
    st.session_state.url = None

if 'execute_pressed' not in st.session_state:
    st.session_state.execute_pressed = False

formatted_text = ""
url = ""

st.title('🤖Typing is all you need!')

# Text input for the main text
input_text = st.text_area('Paste text into box below')

# Function to generate the URL
def convert_open(text, duration_inSec=60, shuffle=0, spell_check=True):
    convert = OConverter(spell_check=spell_check)
    formatted_text = convert.format_text(text)
    url = convert.generate_link(formatted_text, duration_inSec=duration_inSec, shuffle=shuffle)
    return formatted_text, url

# Create placeholders
formatted_text_placeholder = st.empty()
url_placeholder = st.empty()

# Generate the URL if text input is not empty
if input_text:
    duration_inSec = st.slider('Duration in Seconds', min_value=10, max_value=300, value=60)
    shuffle = st.select_slider('Shuffle', options=[0, 1])
    shuffle = int(shuffle)
    spell_check = st.select_slider('Spell Check', options=[0, 1])
    spell_check = int(spell_check)

    st.write(f"Selected Duration: {duration_inSec} seconds")
    st.write(f"Selected Shuffle: {shuffle}")

    if st.button('Execute'):
        st.session_state.execute_pressed = True
        formatted_text, st.session_state.url = convert_open(text=input_text, duration_inSec=duration_inSec, shuffle=shuffle, spell_check=spell_check)

# This part will update the placeholders again if 'execute_pressed' is True.
if st.session_state.execute_pressed:
    formatted_text_placeholder.write(f"Formatted Text: {formatted_text}")
    url_placeholder.write("Generated URL Successfully")

    if st.button('Start typing'):
        st.write(f"Open this link to start typing: [Click here]({st.session_state.url})")
