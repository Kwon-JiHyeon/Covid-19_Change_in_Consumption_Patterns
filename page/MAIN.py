import streamlit as st
from utils import covid_utils as cou
from utils import emart_utils as emu
from utils import consumer_expenditure_utils as ceu
from page import local_folium_map as lfm
from utils import BSI_processing as bp
from utils import sales_processing as sp
from utils import local_currency_mean_proc as lcmp

def app():
    s_box = st.selectbox('프로젝트 내용을 선택하세요.',
                         ('Covid-19 현황', '월평균 가계 소비지출', '지역화폐이용현황(가맹점 지도)', '소상공인 & 전통시장 경기동향', '발달 골목 상권 매출 현황','E-Mart 매출액'))

    if s_box == 'Covid-19 현황':
        cou.covid()
    elif s_box == '월평균 가계 소비지출':
        ceu.spend()    
    elif s_box == '지역화폐이용현황(가맹점 지도)':
        lcmp.proc()
        st.write('\n')
        st.write('신규가입자와 월별 사용액이 늘어나는만큼 지역화폐 가맹점이 얼마나 있는지 알아보겠습니다.')
        lfm.app()
    elif s_box == '소상공인 & 전통시장 경기동향':
        bp.proc()
    elif s_box == '발달 골목 상권 매출 현황':
        sp.proc()
    elif s_box == 'E-Mart 매출액':
        emu.emart()