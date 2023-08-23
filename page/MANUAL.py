import streamlit as st
from page import virtual_environment_manual as vem
from page import streamlit_manual as stm

def app():
    s_box = st.selectbox('확인하고 싶은 메뉴얼을 선택하세요.',('가상환경 구축 메뉴얼', 'streamlit 메뉴얼'))

    if s_box == '가상환경 구축 메뉴얼':
        vem.app()
    elif s_box == 'streamlit 메뉴얼':
        stm.app()
