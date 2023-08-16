import pandas as pd
import matplotlib.pyplot as plt

# 엑셀 파일에서 데이터 읽기
data = pd.read_excel('emart.xlsx')

# '기준년월' 컬럼 파싱하여 '년도'와 '월' 컬럼 생성
data['년도'] = data['기준년월'].str.split('년').str[0].str.strip()
data['월'] = data['기준년월'].str.split('년').str[1].str.replace('월', '').str.strip()

# 년도와 월을 숫자로 변환
data['년도'] = data['년도'].astype(int)
data['월'] = data['월'].astype(int)

# 년도별로 데이터 분류
yearly_data = data.groupby('년도').sum()

# 그래프 그리기
plt.figure(figsize=(12, 12))

# 4개의 그래프 영역 생성
for i, year in enumerate(yearly_data.index):
    plt.subplot(2, 2, i+1)
    plt.plot(data[data['년도'] == year]['월'], data[data['년도'] == year]['매출액(단위:억원)'], marker='o')
    plt.title(f'E-mart Year {year} Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales (억원)')

    # x축 눈금 설정
    plt.xticks(data[data['년도'] == year]['월'])

plt.savefig('emart_years.png')

# 그래프 출력
plt.tight_layout()
plt.show()
