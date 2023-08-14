# 라이브러리 import
import requests
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# url 입력
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey={키값}&apiType=xml&gubun=경기'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text

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

# 그래프 그리기
months = list(monthly_data.keys())
cases = list(monthly_data.values())

plt.figure(figsize=(25, 6))
bars = plt.bar(months, cases, color='skyblue')
plt.title('Monthly number of COVID-19 in Gyeonggi-do')
plt.xticks(rotation=45)
plt.tight_layout()

# y축 눈금 설정
plt.yticks(range(0, max(cases) + 100000, 500000), ["{:,}".format(y) for y in range(0, max(cases) + 100000, 500000)])

# 각 막대 옆에 세 자리마다 컴마가 들어간 확진자 수 표시
for i, bar in enumerate(bars):
    formatted_case = "{:,}".format(cases[i])  # 세 자리마다 컴마 삽입
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), formatted_case,
             ha='center', va='bottom', fontsize=10, color='black')

plt.savefig('covid_cases_total.png')

# 그래프 표시
plt.show()
