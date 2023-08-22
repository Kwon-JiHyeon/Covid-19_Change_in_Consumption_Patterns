import streamlit as st
from utils import emart as em

def app():
	st.header("E-mart Yearly Sales")
	st.subheader('1. Yearly')
	em.emart_plot()

