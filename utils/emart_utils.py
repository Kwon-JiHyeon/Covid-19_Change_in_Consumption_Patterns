import streamlit as st
import os
from PIL import Image
from utils import emart_row as emr

script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
image_dir = os.path.join(script_dir, 'picture')  # 상위 디렉토리의 image 폴더 경로

emart_image1 = Image.open(os.path.join(image_dir, 'emart1.png'))

def emart():
    st.write('\n')
    st.write('\n')
    st.subheader('4개년도 월별 이마트 매출액')
    st.write('월별 이마트 매출액 데이터는 전자공시시스템 포털에서 xlsx파일을 다운받아 csv파일로 변환하여 사용하였습니다.')
    st.write(f'전자공시시스템 : https://dart.fss.or.kr/dsab007/main.do')
    st.write('\n')
    st.write('\n')
    st.write('<b>1. csv파일 생성</b>', unsafe_allow_html=True)
    st.image(emart_image1)
    st.write('먼저 월별로 나뉘어져있는 매출액 xlsx파일을 하나로 합쳐서, csv파일로 저장합니다.')

    st.write('\n')
    st.write('\n')
    st.write('<b>2. 데이터 전처리</b>', unsafe_allow_html=True)
    emr.emart_sales_pd()

    st.write('하나로 합쳐진 csv파일을 파이썬 문법을 사용하여 년/월 기준으로 나누어서 그래프로 표현해 줍니다.')