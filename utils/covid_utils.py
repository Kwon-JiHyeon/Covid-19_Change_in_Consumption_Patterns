import streamlit as st
import os
from PIL import Image
from utils import covid_row as cor

script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
image_dir = os.path.join(script_dir, 'picture')  # 상위 디렉토리의 image 폴더 경로

covid_image1 = Image.open(os.path.join(image_dir, 'covid1.png'))

def covid():
    st.write('\n')
    st.write('\n')
    st.subheader('4개년도 월별 경기도 코로나 현황')
    st.write('월별 경기도 코로나 현황데이터는 공공 데이터 포털에서 OPEN API를 사용하였습니다.')
    st.write(f'보건복지부_코로나19 시도 발생현황 : https://www.data.go.kr/data/15098776/openapi.do')
    st.write('\n')
    st.write('\n')
    st.write('<b>1. OPEN API 인증키 발급 및 경기도 데이터 추출</b>', unsafe_allow_html=True)
    st.image(covid_image1)
    st.write('먼저 발급받은 인증키를 넣고, 경기도 데이터만 추출합니다.')

    st.write('\n')
    st.write('\n')
    st.write('<b>2. 데이터 전처리</b>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write('<b>2-1. 누적 확진자 수</b>', unsafe_allow_html=True)
        cor.covid_accrue()

    with col2:
        st.write('<b>2-2. 월별 확진자 수</b>', unsafe_allow_html=True)
        cor.covid_month()

    st.write('공공데이터에서는 일자별 누적데이터만 제공되어 먼저 월별로 누적데이터를 만들어줍니다.')
    st.write('이후, 파이썬 기본문법과 수학적 수식을 이용하여 월별 확진자수를 추출했습니다.')
    st.write('추출한 데이터로 경기도의 월별 코로나확진자 수 그래프를 그릴 수 있습니다.')


