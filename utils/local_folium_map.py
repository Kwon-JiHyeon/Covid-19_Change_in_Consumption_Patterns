# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:45:53 2023

@author: MAIN
"""

#데이터가 너무 많아 streamlit에서는 실행이 어려워 실제로 쓰지는 않았습니다.

import os
import pandas as pd
import folium
from folium import Marker
from folium.plugins import MarkerCluster
import folium.plugins as plug 

script_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 디렉토리 경로
path_dir = os.path.join(script_dir, 'row_data')
    
#데이터 불러오기, low=memory=False는 column에 NaN값이나 여러 type의 데이터가 섞여 있으면 경고가 뜨는데 경고 메세지가 출력되지 않게 하는 것
data = pd.read_csv(path_dir + f'\\가맹점.csv',low_memory=False)
#1.0은 지금 계속 영업 하는 곳
r_data = data[data['휴폐업상태코드']==1.0]
rr_data = r_data.loc[:,['상호명','위도','경도']]
df = rr_data.dropna(axis=0) #결측값 있는 행 제거

def store():    
    locations = list(zip(rr_data.iloc[:,1], rr_data.iloc[:,2]))
    
    m = folium.Map(location=[37.541, 126.986], zoom_start=12)
    mc = MarkerCluster()

    for _, i in rr_data.iterrows():
        mc.add_child(
                Marker(location = [i['위도'],i['경도']],
                       popup=i['상호명']))
    m.add_child(mc)
    
    m.save('가맹점.html')

#store()을 하면 지도가 저장됩니다.
