import streamlit as st
from PIL import Image
import os
import glob

import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)

import BSI

url_sosang = 'https://www.data.go.kr/data/3060077/fileData.do'
url_trd = 'https://www.data.go.kr/data/3060078/fileData.do'

file_p = os.path.dirname(__file__)
file_path = os.path.join(file_p, 'picture')
pic_dict = {}
for i in range(1,12):
    pic_dict[f'pic{i}'] = Image.open(glob.glob(os.path.join(file_path, f'사진{i}*.png'))[0])

def proc():
    st.write('<b>소상공인 & 전통시장 경기동향</b>', unsafe_allow_html=True)
    st.write('소상공인, 전통시장 경기동향 데이터는 공공 데이터 포털에서 csv형식으로 다운받았습니다.')
    st.markdown(f'소상공인 경기동향 : {url_sosang}')
    st.markdown(f'전통시장 경기동향 : {url_trd}')
    
    st.image(pic_dict['pic1'])
    st.image(pic_dict['pic2'], caption='소상공인 경기동향.csv')
    st.image(pic_dict['pic8'])
    st.image(pic_dict['pic9'], caption='전통시장 경기동향.csv')
    
    st.write('\n')
    st.write('\n')
    col1, col2 = st.columns(2)
    with col1:
        st.write('<b>소상공인 경기동향</b>', unsafe_allow_html=True)
        st.dataframe(BSI.df_copy)
    with col2:
        st.write('<b>전통시장 경기동향</b>', unsafe_allow_html=True)
        st.dataframe(BSI.df_trd_copy)
    
    st.write('두 데이터 모두 연도와 월이 다른 열로 구분돼 있고 전체, 지역, 분야별 경기동향이 있습니다.',
             '또, 2013년 1월부터 2023년 8월까지의 데이터이며 전통시장 경기동향은 2017년 이전 지역 경기동향이 없는걸 알 수 있습니다.')
    
    col3, col4 = st.columns(2)
    with col3:
        st.image(pic_dict['pic7'], caption='소상공인.info()')
    with col4:
        st.image(pic_dict['pic10'], caption='전통시장.info()')
    
    st.write('모두 128개의 행과 72개의 열로 이루어진 데이터입니다.')
    st.write('이제 코로나 긴급 재난 지원금 지원에 따른 경기도 소상공인 & 전통시장 경기동향을 파악하기 위해',
             '코로나 발생 이전인 2019년 9월부터 3차 재난지원금 지급 이후인 2021년 3월까지의 경기도 경기동향 데이터만 추출하겠습니다. 코로나 발생 시기인 2019년 12월부터 하지않는 이유는 코로나 발생이 경기동향 변화에 영향을 주었는지 확인하기 위함입니다.')
    st.write('\n')
    st.write('\n')
    col5, col6 = st.columns(2)
    with col5:
        st.write('<b>소상공인</b>', unsafe_allow_html=True)
        st.dataframe(BSI.df3)
    with col6:
        st.write('<b>전통시장</b>', unsafe_allow_html=True)
        st.dataframe(BSI.df3_trd)
    
    st.write('연도와 월을 합쳐서 인덱스로 보내고 경기체감과 경기전망 열만 모아서 새로운 데이터를 만들었습니다.',
         '데이터를 확인하니 소비패턴의 변화를 확인할 때 경기전망은 필요 없는것 같아서 경기체감만 사용하기로 했습니다.')


