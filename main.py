import streamlit as st
import pandas as pd
import numpy as np
from html_module import line_break, section, callout, title
from PIL import Image

# config
st.set_page_config(
    page_title="COVID-19 Coughing Detector",
    page_icon="π€",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# title
title('COVID-19 Coughing Detector')

# μ½λ‘λ μ¦μ
section('μ½λ‘λ19 μ£Όμ μ¦μ μλ΄')

line_break()

image = Image.open('images/μ½λ‘λμ¦μ.png')
st.image(image,)

line_break()

st.markdown('μ¬λ¬λΆμ΄ μκ³  μλ μ¦μμ λ¬΄μμΈκ°μ?')
agree1 = st.checkbox('λ°μ΄')
agree2 = st.checkbox('κΈ°μΉ¨')
agree3 = st.checkbox('λͺΈμ΄')
agree4 = st.checkbox('μΈνν΅')

if agree1 or agree2 or agree3 or agree4:
    st.markdown('μ½λ‘λ19 μ¦μμ΄ μκ΅°μ! μ½λ‘λ κ²μ¬κ° νμν  κ² κ°μμ.')

line_break()
line_break()

callout(['νμ¬ μ§μ μ§λ¨ν€νΈκ° μμΌμ κ°μ?',
         '',
        'COVID-19μ λλλ¬μ§ μ¦μμ κΈ°μΉ¨κ³Ό νΈν‘ κ³€λμ ν¬ν¨ν©λλ€.',
         'AI κΈ°μ μ νμ©νμ¬ κΈ°μΉ¨ μλ¦¬λ‘λΆν° COVID-19μ λν μ μ©ν ν΅μ°°λ ₯μ μ»μ μ μμ΅λλ€.',
         'κΈ°μΉ¨ μλ¦¬λ‘λΆν° COVID-19λ₯Ό κ²μΆνλ μλ‘μ΄ μ§λ¨ λκ΅¬λ₯Ό μ¬μ©ν΄λ³΄μΈμ!'])

line_break()
line_break()
line_break()

# step
section('μ§λ¨ λκ΅¬ μ¬μ© λ°©λ²')
line_break()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        #### Step1
        κΈ°μΉ¨ μλ¦¬λ‘λΆν° COVID-19λ₯Ό κ²μΆνλ μλ‘μ΄ μ§λ¨ λκ΅¬λ₯Ό μ¬μ©ν΄λ³΄μμ.
        """
    )
    st.image("images/step1.jpg")

with col2:
    st.markdown(
        """
        #### Step2
        κΈ°μΉ¨νλ μλ¦¬λ₯Ό λΉμν©λλ€.
        λΉμ νμΌμ νμ₯μλͺμ **WAV**μ΄μ΄μΌ ν©λλ€!
        λ€λ₯Έ νμ₯μλλΌλ μλ λ³νλ©λλ€.
        """
    )
    st.image("images/step2.jpg")

with col3:
    st.markdown(
        """
        #### Step3
        COVID-19 Detection νμ΄μ§μμ μ§λ¨ κ²°κ³Όλ₯Ό νμΈνμΈμ!
        """
    )
    st.image("images/step3.jpg")
