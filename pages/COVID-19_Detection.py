import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa

st.set_page_config(layout="wide")

CFG = {
    'SR': 16000,     # 주파수(Sample_rate)
    'N_MFCC': 15,    # MFCC 벡터를 추출할 개수
    'SEED': 41,      # 시드(Random Seed)
    'N_MELS': 128    # 고주파 대역 스케일(Mel Scale)
}


def wav_plot(y, sr):
    time = np.linspace(0, len(y)/sr, len(y))
    fig, ax = plt.subplots(figsize=(5,5))
    ax.plot(time, y, color='g')
    ax.set_xlabel('Time')
    ax.set_ylabel('Voice')
    plt.title('WAV Plot')
    st.pyplot(fig)


def judge_covid():
    y, sr = librosa.load(audio_file, sr=CFG['SR'])
    wav_plot(y, sr)


audio_file = st.file_uploader("Upload Images", type=["wav", "mp3", "mp4"])

if audio_file is not None:
    if st.button('Submit audio file'):
        judge_covid()


covid_result = st.radio('COVID-19 Result', [0, 1])


if covid_result == 0:
    st.header('검진결과 코로나 음성입니다!')
    st.write('개인 방역을 철저히 하시고 경과를 더 지켜봅시다!')
else:
    st.header('검진결과 코로나 양성입니다!')
    st.write('아래의 안내문을 참고하여 자가격리를 해주세요!')

    tab1, tab2, tab3 = st.tabs(
        ["재택치료 안내문(집중관리군)", "재택치료 안내문(일반관리군)", "재택치료자 동거인 안내문"])
    with tab1:
        st.header("재택치료 안내문(집중관리군)")

        st.image('images/재택치료 안내문(집중관리군).jpg')

    with tab2:
        st.header("재택치료 안내문(일반관리군)")

        st.image('images/재택치료 안내문(일반관리군).jpg')

    with tab3:
        st.header("재택치료 동거인 안내문")

        st.image('images/동거인안내문.png')
