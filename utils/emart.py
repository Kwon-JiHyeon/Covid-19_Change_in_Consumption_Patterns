import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

def emart():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트 파일의 디렉토리 경로
    path_dir = os.path.join(script_dir, 'row_data')

    # 엑셀 파일에서 데이터 읽기
    data = pd.read_csv(os.path.join(path_dir, 'emart.csv'))

    # '기준년월' 컬럼 파싱하여 '년도'와 '월' 컬럼 생성
    data['년도'] = data['기준년월'].str.split('년').str[0].str.strip()
    data['월'] = data['기준년월'].str.split('년').str[1].str.replace('월', '').str.strip()

    # 년도와 월을 숫자로 변환
    data['년도'] = data['년도'].astype(int)
    data['월'] = data['월'].astype(int)

    # 년도별로 데이터 분류
    yearly_data = data.groupby('년도').sum(numeric_only=True)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    return yearly_data, data
    
def emart_plot():
    yearly_data, data = emart()    
    plt.figure(figsize=(12, 12))

    # 4개의 그래프 영역 생성
    for i, year in enumerate(yearly_data.index):
        plt.subplot(2, 2, i + 1)
        subset = data[data['년도'] == year]
        plt.plot(subset['월'], subset['매출액(단위:억원)'], marker='o')
        plt.title(f'E-mart Year {year} Sales')
        plt.xlabel('Month')
        plt.ylabel('Sales (억원)')

        # x축 눈금 설정
        plt.xticks(subset['월'])

    st.pyplot(plt)

def emart_one_plot():
    yearly_data, data = emart()
    data = data[data['년도'] == 20]
    fig=plt.figure(figsize=(15,6))
    ax = fig.add_subplot(1,1,1)
    ax.plot(data['월'], data['매출액(단위:억원)'], marker='o')
    ax.set_xticks(data['월'])
    ax.set_title('2020 year E-mart sales')
    ax.set_xlabel('month')
    ax.set_ylabel('100 million')
    return fig