import streamlit as st
from PIL import Image
import os

def app():
    st.header('가상환경 구축방법')

    st.subheader('1. 가상환경이란')

    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
    image_dir = os.path.join(script_dir, 've_image')  # 상위 디렉토리의 image 폴더 경로

    env_image1 = Image.open(os.path.join(image_dir, 'image1.png'))
    env_image2 = Image.open(os.path.join(image_dir, 'image2.png'))
    env_image3 = Image.open(os.path.join(image_dir, 'image3.png'))
    env_image4 = Image.open(os.path.join(image_dir, 'image4.png'))
    env_image5 = Image.open(os.path.join(image_dir, 'image5.png'))
    env_image6 = Image.open(os.path.join(image_dir, 'image6.png'))
    env_image7 = Image.open(os.path.join(image_dir, 'image7.png'))

    st.write('''시스템에 설치된 파이썬과 별도로 다른 디렉토리에 파이썬 인터프리터와 파이썬 라이브러리를 설치한 것을 의미합니다. 
             powershell prompt를 들어가면 지금 어떤 환경을 쓰고 있는지 보입니다.''')
    st.image(env_image1)


    st.subheader('2.가상환경 구축하기')
    st.image(env_image2)
    st.write('''가상환경을 구축하기 위해서는 위와같은 코드를 입력해줍니다.
             밑줄에는 가상환경 이름을 입력해주시면 됩니다.''')
    st.image(env_image3)
    st.write('Proceed가 나오면 y를 치고 Enter키를 눌러줍니다.')
    st.image(env_image4)
    st.write('위와 같은 말이 나오면 정상적으로 환경구축이 완료된 것입니다.')
    st.image(env_image5)
    st.write('''가상환경이 잘 구축되었는지 확인하는 또 다른 방법은 가상환경리스트를 보는 것입니다.''')
    st.image(env_image6)
    st.write('가상환경으로 들어가면 위와 같은 코드를 입력하면 되고 맨 앞이 바뀐다면 가상환경이 변경된 것입니다.')
    st.image(env_image7)
    st.write('가상환경을 나오고 싶다면 위와같은 코드를 입력하면 됩니다.')

