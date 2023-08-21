import streamlit as st
import os
from PIL import Image
from utils import consumer_expenditure_row as cer

script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
image_dir = os.path.join(script_dir, 'picture')  # 상위 디렉토리의 image 폴더 경로

spend_image1 = Image.open(os.path.join(image_dir, 'spend1.png'))

def spend():
    st.write('\n')
    st.write('\n')
    st.subheader('4개년도 분기별 가계 소비지출 현황')
    st.write('분기별 가계 소비지출 현황데이터는 Kosis 포털에서 csv파일을 다운받아 사용하였습니다.')
    st.write(f'Kosis 가구당 월평균 가계수지: https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1L9U001&vw_cd=MT_ZTITLE&list_id=G_A_10_003_001&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE')
    st.write('\n')
    st.write('\n')
    st.write('<b>1. 데이터를 csv파일로 다운</b>', unsafe_allow_html=True)
    st.image(spend_image1)
    st.write('csv로 받은 파일에서 필요한 데이터를 확인합니다. 코로나 전후 가계당 소비가 줄었는지 늘었는지 비교하기 위해'
             '전체가구를 기준으로 소비지출 데이터만 추출할 예정입니다. ')

    st.write('\n')
    st.write('\n')
    st.write('<b>2. 데이터 전처리</b>', unsafe_allow_html=True)
    cer.spend_pd()


    st.write('월평균 가계수지 데이터는 열에 전체가구, 근로가구, 근로외 가구가 나뉘어져있는데 '
             '전반적인 소비패턴을 파악하기 위해 전체가구에서 추출하였습니다. 이렇게 추출한 데이터로 matplotlib을 사용하여 그래프를 그려주었습니다.')


