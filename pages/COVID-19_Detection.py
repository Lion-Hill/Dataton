import streamlit as st
import numpy as np
import pandas as pd
import librosa
import pickle
import warnings
import os
from pydub import AudioSegment

warnings.filterwarnings(action='ignore')

st.set_page_config(layout="wide")

CFG = {
    'SR': 16000,     # 주파수(Sample_rate)
    'N_MFCC': 32,    # MFCC 벡터를 추출할 개수
    'SEED': 41,      # 시드(Random Seed)
    'N_MELS': 128    # 고주파 대역 스케일(Mel Scale)
}

symptoms = {
    '있다': 1,
    '없다': 0
}


def get_mfcc_feature():
    st.write(audio_file)
    file_name = audio_file.name.split('.')[0]
    extension = audio_file.name.split('.')[1]
    if extension == 'mp4':
        st.write('mp4')
        audio_file = AudioSegment.from_file(audio_file.name, 'mp4').export(
            os.path(audio_file.name+".wav"), format="wav")
    elif extension == 'm4a':
        st.write('m4a')
    elif extension == 'mp3':
        st.write('mp3')
    elif extension == 'wav':
        st.write('wav')
    else:
        st.write('파일 형식에 맞는 파일을 올려주세요!!')

    y, sr = librosa.load(audio_file, sr=CFG['SR'])
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=CFG['N_MFCC'])
    y_feature = []
    for e in mfcc:
        y_feature.append(np.mean(e))
    mfcc_df = pd.DataFrame(y_feature).T
    return mfcc_df


def data_preprocessing():
    info_df = pd.DataFrame(data={'age': [int(age_info)], 'respiratory_condition': [symptoms[respiratory_condition]],
                           'fever_or_muscle_pain': [symptoms[fever_or_muscle_pain]]})
    sex_df = pd.DataFrame(
        data={'female': [0], 'male': [0], 'other': [0]})

    if sex_info == '남성':
        sex_df['male'] = 1
    elif sex_info == '여성':
        sex_df['female'] = 1
    else:
        sex_df['other'] = 1

    return info_df, sex_df

# 모델 load하는 함수


def get_model():
    model = pickle.load(open('model/mlp_second.sav', 'rb'))
    return model


def judge_covid():
    mfcc_df = get_mfcc_feature()
    info_df, sex_df = data_preprocessing()
    mid_df = pd.merge(info_df, mfcc_df, left_index=True, right_index=True)
    result_df = pd.merge(mid_df, sex_df, left_index=True, right_index=True)
    # wav_plot(y, sr)
    model = get_model()
    sample_proba = 0.14
    sample_data = np.array(result_df).reshape(1, -1)
    sample_pred = model.predict_proba(sample_data)[:, 1][0]
    sample_result = np.where(sample_pred < sample_proba, 0, 1)
    sample_return = np.array(['Negative', 'Positive'])[sample_result]
    return sample_return


audio_file = st.file_uploader("Upload Audio file", type=[
                              "wav", "mp3", "mp4", "m4a"])
age_info = st.number_input(
    'Input your age', min_value=1, max_value=100, step=1)
sex_info = st.selectbox('성별을 골라주세요', ('남성', '여성', '기타'))
respiratory_condition = st.selectbox(
    '현재 호흡기 질병 증상이 있으신가요?', ('있다', '없다'))
fever_or_muscle_pain = st.selectbox(
    '현재 발열증상이나 근육통 증상이 있으신가요?', ('있다', '없다'))


if (audio_file is not None):
    if st.button('Submit audio file'):
        sample_return = judge_covid()

        if sample_return == 'Negative':
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
