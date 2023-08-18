import streamlit as st
from page import Project_Direction as pjd
from page import MANUAL as MANU
from page import diagram as dia
from page import MAIN
from page import result_page as rp


semi_header = f'Covid-19 시국 정부의 재난지원금 제공에 따른 경기도 지역 소상공인, 전통시장 실적과 소비 패턴의 변화'

item = st.sidebar.selectbox('데이터 시각화&분석 취업캠프 세미 프로젝트', ['메인','프로젝트 수행 방향', '프로젝트 구축 메뉴얼', '프로젝트 Diagram',
														'프로젝트 내용(데이터 전처리)', '프로젝트 결과'])

if item == '메인':
	st.title('데이터 시각화&분석 취업캠프(Python) 세미 프로젝트')
	st.header(semi_header)
	st.write('조장: 권지현(기획안 작성, 데이터 수집 전처리, 분석, 시각화, 포트폴리오 작성)')
	st.write('조원1: 강예진(데이터 수집, 전처리, 분석, 시각화, 발표)')
	st.write('조원2: 권용현(데이터 수집, 전처리, 분석, 시각화)')
elif item == '프로젝트 수행 방향':
	st.header(semi_header)
	pjd.app()
elif item == '프로젝트 구축 메뉴얼':
	MANU.app()
elif item == '프로젝트 Diagram':
	st.header(semi_header)
	dia.app()
elif item == '프로젝트 내용(데이터 전처리)':
	st.header(semi_header)
	MAIN.app()
elif item == '프로젝트 결과':
    st.header(semi_header)
    rp.app()
