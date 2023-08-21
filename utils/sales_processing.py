# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:07:55 2023

@author: rnjsd
"""
import sys
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)

import streamlit as st
import sales
from PIL import Image
import os
import glob

url = 'https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=B7BIA8NM4VIXSPPQQV0132089283&infSeq=3&order=&loc=&searchWord=%EA%B3%A8%EB%AA%A9'

file_p = os.path.dirname(__file__)
file_path = os.path.join(file_p, 'picture')
pic_dict = {}
for i in range(1,12):
    pic_dict[f'pic{i}'] = Image.open(glob.glob(os.path.join(file_path, f'사진{i}*.png'))[0])

def proc():
    st.write('<b>2020년 골목 발달 상권 매출 현황</b>', unsafe_allow_html=True)
    
    st.write('발달 골목 상권 데이터는 경기데이터드림에서 csv형식으로 다운받았습니다.')
    st.markdown(f'발달 골목 상권 : {url}')
    st.image(pic_dict['pic11'], caption='발달 골목 상권.csv')
    st.dataframe(sales.df_sales)
    st.write('매출 금액과 매출 건수는 BC카드 데이터를 기반으로 추정된 값입니다.')
    st.write('소상공인은 상시근로자 기준 제조업·건설업·운송업은 10인 미만, 도소매업·서비스업은 5인 미만이라는 조건이있으나 이 데이터에선 상시근로자 인원을 알수 없으니 전부 소상공인, 전통시장으로 가정하고 합니다. ')
    st.write('위 데이터를 확인해보니 분기별 산업에 따른 매출금액과 매출건수로 이루어져있습니다.',
             '분기별로 매출금액과 매출건수를 알아보기위해 각 분기별로 매출금액과 매출건수의 총합을 구해봤습니다.')
    st.dataframe(sales.result_df)

