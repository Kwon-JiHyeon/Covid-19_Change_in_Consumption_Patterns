# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:21:28 2023

@author: rnjsd
"""
import local_currency_mean as lcm
import streamlit as st
from PIL import Image
import os
import glob


url = 'https://data.gg.go.kr/portal/adjust/service/selectHisServicePage.do?infId=6FEDD6KGEJWYCY2G15OY29527318&infSeq=1&hisBsDt=20230630#none'

path = os.path.dirname(__file__)
file_path = os.path.join(path, 'picture')
pic_dict = {}
for i in range(1,13):
    pic_dict[f'pic{i}'] = Image.open(glob.glob(os.path.join(file_path, f'사진{i}*.png'))[0])

def proc():
    st.write('<b>지역화폐 발행 및 이용 현황</b>', unsafe_allow_html=True)
    st.write('지역화폐 발행 및 이용 현황 데이터는 경기데이터드림에서 csv형식으로 다운받았습니다.')
    st.markdown(f'지역화폐 발행 및 이용 현황 : {url}')
        
    st.image(pic_dict['pic12'], caption='지역화폐 발행 및 이용 현황.csv')
    st.dataframe(lcm.df_local)
    st.write('데이터를 확인해보면 시흥, 김포시는 전부 비었고 성남시는 신규가입자수 부분만 비어있습니다. 하지만 우리는 단순히 더하는 작업만 할거기 때문에 따로 결측값 제외하는 작업은 하지 않고 진행하겠습니다.')
    st.dataframe(lcm.df2_local)
    st.write('기준년월의 정렬이 내림차순으로 되어있기때문에 보기좋게 오름차순으로 바꿔주었습니다.')
    st.dataframe(lcm.new_mean_df2_local)
    st.write('각 월마다 신규가입자, 충전액, 사용액을 알기위해 모든 도시를 월별로 합쳐주었습니다.')