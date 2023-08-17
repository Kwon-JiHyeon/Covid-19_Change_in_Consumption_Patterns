import pandas as pd
import matplotlib.pyplot as plt

# 데이터 파일 불러오기 (EUC-KR 인코딩)
data = pd.read_csv('spend.csv', encoding='EUC-KR')

# 전체가구 소비지출만 추출
spending_data = data[data.columns[1::3]].iloc[12]

# spending_data를 정수형으로 변환
spending_data = spending_data.str.replace(',', '').astype(int)

# 그래프 그리기
plt.figure(figsize=(12, 8))
plt.plot(spending_data.index, spending_data.values, marker='o')
plt.title('Total Household Expenditure')
plt.xlabel('Year/Quarte')
plt.ylabel('Consumption Expenditure')
plt.xticks(rotation=45)

plt.savefig('Total_Household_Expenditure.png')
plt.show()
