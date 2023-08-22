import streamlit as st
from PIL import Image
import os

def app():
    st.write('\n')
    st.write('\n')
    st.write('<b>프로젝트 Diagram은 drawio프로그램으로 작성되었습니다.<b>', unsafe_allow_html=True)
    st.write('\n')
    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
    image_dir = os.path.join(script_dir, 'image')  # 상위 디렉토리의 image 폴더 경로
    dia_image1 = Image.open(os.path.join(image_dir, 'semi_diagram.drawio.png'))
    st.image(dia_image1)
