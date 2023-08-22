import streamlit as st
from utils import consumer_expenditure as ce

def app():
	st.header("분기별 전체가구 소비지출")
	ce.spend()

