# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:44:14 2023

@author: MAIN
"""
import streamlit as st
import os
from PIL import Image
from utils import local_folium_map as local



def app():
    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
    image_dir = os.path.join(script_dir, 'folium_image')
    pic_dict = {}
    for i in range(1,6):
        pic_dict[f'f_image{i}'] = Image.open(image_dir + f'\\folium_image{i}.png')
    
    url = 'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&sortColumn=&sortDirection=&infId=3NPA52LBMO36CQEQ1GMY28894927&infSeq=1&searchWord=%EC%A7%80%EC%97%AD%ED%99%94%ED%8F%90+%EA%B0%80%EB%A7%B9%EC%A0%90'

    st.write('<b>지역화폐 가맹점 현황</b>', unsafe_allow_html=True)
    st.write('지역화폐 가맹점 데이터는 경기도 데이터드림 포털에서 csv형식으로 다운받았습니다.')
    st.markdown(f'지역화폐 가맹점 데이터 : {url}')
    #st.image(pic_dict['f_image1'])
    st.dataframe(local.data)
    st.write('''휴업상태코드 == 1 : 계속사업자, 휴업상태코드 == 2 : 휴업자, 휴업상태코드 == 3 : 폐업자를 뜻합니다.\n''')
    st.image(pic_dict['f_image2'])
    st.write('''위와 같은 코드로 필요한 변수인 상호명,위도,경도 열만 골라내고 결측값이 있으면
             행을 삭제하는 방법으로 전처리를 진행하였습니다''')
    st.dataframe(local.df)
    
    st.write('<b>가맹점 지도 그리기</b>', unsafe_allow_html=True)
    st.write('''데이터가 너무 많아 일일이 표시를 하면 가독성이 떨어지기 때문에
             MarkerCluster라는 비슷한 위치에 있으면 묶어주는 라이브러리를 사용했습니다.''')
    
    st.image(pic_dict['f_image3'])
    st.image(pic_dict['f_image5'],
             caption='지도는 시간이 오래걸려 이미지파일로 대체합니다.')
    
    