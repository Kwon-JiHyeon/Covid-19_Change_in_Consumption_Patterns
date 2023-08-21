import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'row_data', 'spend.csv')
data = pd.read_csv(csv_path, encoding='EUC-KR')

def spend_graph():
    # Extract total household expenditure
    spending_data = data[data.columns[1::3]].iloc[12]
    spending_data = spending_data.str.replace(',', '').astype(int)

    # Create the plot using matplotlib
    plt.figure(figsize=(12, 8))
    plt.plot(spending_data.index, spending_data.values, marker='o')
    plt.title('Total Household Expenditure')
    plt.xlabel('Year/Quarter')
    plt.ylabel('Consumption Expenditure')
    plt.xticks(rotation=45)

    # Display the plot in Streamlit
    st.pyplot(plt)

def spend_pd():
    # 전체가구 소비지출만 추출
    spending_data = data[data.columns[1::3]].iloc[12]

    # spending_data를 정수형으로 변환
    spending_data = spending_data.str.replace(',', '').astype(int)

    # 결과를 Pandas DataFrame으로 반환
    data_frame = pd.DataFrame({'Year/Quarte': spending_data.index, 'Consumption Expenditure': spending_data.values})

    # Streamlit에 데이터 표출
    st.write(data_frame)