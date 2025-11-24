import streamlit as st
from gtts import gTTS
from IPython.display import Audio

st.title("Convert Text To Speech")
user_text=st.text_input("Enter text here")
st.button("Convert")

if user_text:
    text_to_speech=gTTS(user_text,lang='hi',tld='com')
    text_to_speech.save('text_to_speech_1.wav')
    sound_file='text_to_speech_1.wav'
    st.audio(sound_file, format="audio/wav")