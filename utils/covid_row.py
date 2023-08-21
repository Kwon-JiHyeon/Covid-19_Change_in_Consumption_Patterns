import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from collections import defaultdict

url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey=OP5oRQ0Ep6V2631jUaL%2FrMqEtiOovCDEBCPnQFYmEneql3ev9DwB6PjiI3Uj%2BocsmFbJaURZkS3uvarZYX4TaA%3D%3D&apiType=xml&gubun=경기'
response = requests.get(url)
contents = response.text
xml_data = contents
root = ET.fromstring(xml_data)
items = root.findall('.//item')
sorted_items = sorted(items, key=lambda item: item.find('stdDay').text)

def covid_total():
    monthly_data = {}
    previous_total_cases = 0

    for item in sorted_items:
        std_day = item.find('stdDay').text
        year, month, _ = std_day.split('-')
        total_cases = int(item.find('defCnt').text)

        month_key = f"{year}-{month}"
        if month_key not in monthly_data:
            monthly_data[month_key] = total_cases - previous_total_cases
        else:
            monthly_data[month_key] += total_cases - previous_total_cases

        previous_total_cases = total_cases

    months = list(monthly_data.keys())
    cases = list(monthly_data.values())

    plt.figure(figsize=(20, 6))
    bars = plt.bar(months, cases, color='skyblue')
    plt.title('Monthly number of COVID-19 in Gyeonggi-do')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.yticks(range(0, max(cases) + 100000, 500000), ["{:,}".format(y) for y in range(0, max(cases) + 100000, 500000)])

    for i, bar in enumerate(bars):
        formatted_case = "{:,}".format(cases[i])
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), formatted_case,
                 ha='center', va='bottom', fontsize=10, color='black')

    st.pyplot(plt)

def covid_years():
    monthly_data = {}
    previous_total_cases = 0

    for item in sorted_items:
        std_day = item.find('stdDay').text
        year, month, _ = std_day.split('-')
        total_cases = int(item.find('defCnt').text)

        month_key = f"{year}-{month}"
        if month_key not in monthly_data:
            monthly_data[month_key] = total_cases - previous_total_cases
        else:
            monthly_data[month_key] += total_cases - previous_total_cases

        previous_total_cases = total_cases

    yearly_data = {'2020': [], '2021': [], '2022': [], '2023': []}

    for month, case in monthly_data.items():
        year = month.split('-')[0]
        yearly_data[year].append((month, case))

    st.set_option('deprecation.showPyplotGlobalUse', False)

    fig, axs = plt.subplots(2, 2, figsize=(15, 15))

    for i, (year, monthly_cases) in enumerate(yearly_data.items()):
        months = [data[0] for data in monthly_cases]
        cases = [data[1] for data in monthly_cases]

        ax = axs[i // 2, i % 2]  # 현재 subplot 가져오기
        bars = ax.bar(months, cases, color='skyblue')
        ax.set_title(f'Monthly number of COVID-19 in Gyeonggi-do - {year}')
        ax.tick_params(axis='x', rotation=45)

        # y축 눈금 설정
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

        # 각 막대 옆에 세 자리마다 컴마가 들어간 확진자 수 표시
        for bar in bars:
            formatted_case = "{:,}".format(bar.get_height())  # 세 자리마다 컴마 삽입
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), formatted_case,
                    ha='center', va='bottom', fontsize=10, color='black')

    st.pyplot(fig)

def covid_month():
    # XML 데이터
    xml_data = contents

    # XML 파싱
    root = ET.fromstring(xml_data)

    # 날짜를 기준으로 데이터 정렬
    items = root.findall('.//item')
    sorted_items = sorted(items, key=lambda item: item.find('stdDay').text)

    # 월별 확진자 수 계산
    monthly_data = {}
    previous_total_cases = 0

    for item in sorted_items:
        std_day = item.find('stdDay').text
        year, month, _ = std_day.split('-')
        total_cases = int(item.find('defCnt').text)

        month_key = f"{year}-{month}"
        if month_key not in monthly_data:
            monthly_data[month_key] = total_cases - previous_total_cases
        else:
            monthly_data[month_key] += total_cases - previous_total_cases

        previous_total_cases = total_cases

    # 결과를 DataFrame으로 변환
    data = {'월': [], '월별 확진자수': []}
    for month, cases in monthly_data.items():
        data['월'].append(month)
        data['월별 확진자수'].append(cases)

    df = pd.DataFrame(data)

    # 결과 출력
    st.write(df)

def covid_accrue():
    # XML 데이터
    xml_data = contents

    # XML 파싱
    root = ET.fromstring(xml_data)

    # 월별 데이터를 저장할 딕셔너리 초기화
    monthly_cases = defaultdict(int)

    # 모든 <item> 요소 선택
    items = root.findall('.//item')

    # 데이터 처리 및 월별 누적 확진자수 계산
    for item in items:
        std_day = item.find('stdDay').text
        def_cnt = int(item.find('defCnt').text)

        year, month, _ = std_day.split('-')
        month_key = f"{year}-{month}"

        # 해당 월의 누적 확진자수 더하기
        monthly_cases[month_key] += def_cnt

    # 정렬된 월별 확진자수 데이터를 DataFrame으로 변환
    data = {'월': [], '월별 확진자수': []}
    sorted_monthly_cases = dict(sorted(monthly_cases.items(), key=lambda item: item[1]))
    for month, cases in sorted_monthly_cases.items():
        data['월'].append(month)
        data['월별 확진자수'].append(cases)

    df = pd.DataFrame(data)

    # Streamlit에 데이터 표출
    st.write(df)