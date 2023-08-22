import streamlit as st
from PIL import Image
import os

def app():
    st.header('streamlit 메뉴얼')
    st.write('<b>Streamlit</b>은 Machine learning과 Data science project에서 사용자가 <b>Web 애플리케이션을 쉽게 생성하고 공유할 수 있는</b>',
             '<b>Python 오픈 소스 라이브러리</b>입니다.',unsafe_allow_html=True)
    st.subheader('1. streamlit 설치 및 실행 방법')

    script_dir = os.path.dirname(__file__)  # 현재 스크립트 파일의 디렉토리 경로
    image_dir = os.path.join(script_dir, 'st_image')
    pic_dict = {}
    for i in range(1,38):
        pic_dict[f'a{i}'] = Image.open(image_dir + f'\\사진{i}.jpg')
    
    
    st.write('아나콘다 파워쉘 프롬프트를 기준으로 설명하겠습니다.',
             '프롬프트에 <b>pip install streamlit</b> 입력하고 실행하세요',unsafe_allow_html=True)
    st.image(pic_dict['a1'])
    
    st.write('아래처럼 나오면 설치가 끝난것입니다.')
    st.image(pic_dict['a13'])
    
    st.write('설치가 완료된 후 <b>streamlit hello</b>를 입력하고 실행하고 웹 페이지가 나오는지 확인하세요.',unsafe_allow_html=True)
    st.image(pic_dict['a2'])
    st.image(pic_dict['a3'])
    
    st.write('혹은 <b>python</b>으로 들어가서 <b>import streamlit</b>이 실행되는지 확인해도됩니다.',unsafe_allow_html=True)
    st.image(pic_dict['a4'])
    
    st.write('확인 작업이 잘 끝났다면 streamlit 설치는 완료입니다.')
    st.write('만약, streamlit 삭제를 원하신다면 <b>pip uninstall streamli</b> 실행하면 됩니다.', unsafe_allow_html=True)
    st.image(pic_dict['a14'])
    
    st.write("<b>streamlit run '파이썬파일'</b> 을통해 실행할 수 있습니다.", unsafe_allow_html=True)
    st.image(pic_dict['a6'])
    
    st.write('예를들어 st.title()을 이용하여 Hello World! 라는 문구가 들어간 파이썬 파일을',
    	'실행하면 아래 화면이 나옵니다.')
    st.image(pic_dict['a5'])
    st.image(pic_dict['a7'])
    st.write('코드 수정시 rerun과 always rerun이 나오는데 수정사항이 적용된 상태에서 재실행을 의미합니다. rerun은 직접 눌러줘야하고, always rerun은 실시간으로 수정사항이 적용됩니다.') 
    st.image(pic_dict['a8'])
    st.image(pic_dict['a9'])
    st.image(pic_dict['a10'])
    st.write('웹 페이지 표출을 멈추고 싶으면 프롬프트에서 Ctrl+c 를 눌러주면 됩니다.')
    st.write('이 때, 웹을 먼저 종료하면 Ctrl+c 가 먹히지 않아 프롬프트를 재실행 해야 합니다.')
    st.image(pic_dict['a15'])
    
    st.header('2. 사용예제')
    st.write('몇 가지 간단한 사용예제를 확인하겠습니다. 원하는 부분을 선택해주세요.')
       
    s_box = st.selectbox('원하는 부분을 고르세요',
		     ('st.title/header/write', 'st.dataframe', 'st.pyplot', 'st.button/checkbox/selectbox','st.text/number/date/time_input, st.text_area', 'folium_static', 'st.sidebar'))
    if s_box == 'st.title/header/write':
        st.write('<b>st.title()</b> : 큰 제목을 표시하는 데 사용됩니다. 화면 상단에 제목을 보여주며 주로 앱이나 섹션의 주요 주제를 강조하는 데 사용됩니다.', unsafe_allow_html=True)
        st.write('<b>st.header()</b> : 더 작은 크기의 제목을 표시하는 데 사용됩니다. 주로 섹션 또는 부분적인 내용을 구분하는 데 활용됩니다.', unsafe_allow_html=True)
        st.write('<b>st.write()</b> : 일반 텍스트를 표시하는 데 사용됩니다. 텍스트 외에도 숫자, 리스트, 테이블, 이미지 등 다양한 유형의 내용을 표시할 수 있습니다.', unsafe_allow_html=True)
        st.image(pic_dict['a16'])
        st.image(pic_dict['a17'])
    elif s_box == 'st.dataframe':
    	st.write('<b>st.dataframe()</b> : 데이터프레임을 시각화하여 웹에서 표시할 수 있게 해주는 기능입니다.', unsafe_allow_html=True)
    	st.write('width:가로길이, height:세로길이, hide_index:인덱스 숨김 유무, column_order:열의 정렬과 특정 열만 표시')
    	st.image(pic_dict['a18'])
    	st.image(pic_dict['a19'])
    elif s_box == 'st.pyplot':
    	st.write('<b>st.pyplot()</b> : 그래프와 차트를 웹에서 표시할 수 있게 해주는 기능입니다.', unsafe_allow_html=True)
    	st.image(pic_dict['a20'])
    	st.image(pic_dict['a21'])
    elif s_box == 'st.button/checkbox/selectbox':
    	st.write('<b>st.button()</b> : 웹에서 버튼을 생성하고 이를 통해 사용자와의 상호 작용을 가능하게 해주는 기능입니다.', unsafe_allow_html=True)
    	st.write('<b>st.checkbox()</b> : 웹에서 체크박스를 생성하고 사용자의 선택 여부에 따라 다양한 동작을 수행할 수 있게 해주는 기능입니다.', unsafe_allow_html=True)
    	st.write('<b>st.selectbox()</b> : 웹에서 선택 상자(드롭다운 메뉴)를 생성하고 사용자가 항목을 선택할 수 있게 해주는 기능입니다.', unsafe_allow_html=True)
    	st.image(pic_dict['a22'])
    	st.image(pic_dict['a23'])
    	st.image(pic_dict['a24'])
    	st.image(pic_dict['a25'])
    	st.image(pic_dict['a26'])
    	st.image(pic_dict['a27'])
    elif s_box == 'st.text/number/date/time_input, st.text_area':
    	st.write('<b>st.text_input()</b> :  웹에서 텍스트를 입력받을 수 있는 입력 위젯(Widget)을 생성하는 함수입니다.', unsafe_allow_html=True)
    	st.write('<b>st.number_input()</b> : 숫자 입력 위젯(Widget)을 생성하는 함수입니다.', unsafe_allow_html=True)
    	st.write('<b>st.date_input()</b> : 날짜 입력 위젯(Widget)을 생성하는 함수입니다.', unsafe_allow_html=True)
    	st.write('<b>st.timer_input()</b> : 시간 입력 위젯(Widget)을 생성하는 함수입니다.', unsafe_allow_html=True)
    	st.write('<b>st.text_area()</b> : 텍스트 영역 입력 위젯(Widget)을 생성하는 함수입니다.', unsafe_allow_html=True)
    	st.image(pic_dict['a28'])
    	st.image(pic_dict['a29'])
    	st.image(pic_dict['a30'])
    	st.image(pic_dict['a31'])
    	st.image(pic_dict['a32'])
    	st.image(pic_dict['a33'])
    	st.image(pic_dict['a34'])
    	st.image(pic_dict['a35'])
    elif s_box == 'folium_static':
    	st.write('<b>folium_static()</b> :  Folium 라이브러리를 사용하여 생성한 지도를 Streamlit 웹 애플리케이션에 쉽게 표시할 수 있게 해주는 함수입니다.', unsafe_allow_html=True)
    	st.image(pic_dict['a36'])
    	st.image(pic_dict['a37'])
    elif s_box == 'st.sidebar':
        st.write('<b>st.sidebar()</b> :  웹의 사이드바에 컨트롤 요소를 추가하여 사용자와 상호 작용할 수 있는 기능을 제공하는 역할을 합니다.', unsafe_allow_html=True)
        st.image(pic_dict['a11'])
        st.image(pic_dict['a12'])


