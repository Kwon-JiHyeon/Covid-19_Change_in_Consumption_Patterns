# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:18:02 2023

@author: MAIN
"""

import os
import sys
module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)

import BSI
import Covid as co
import emart
import consumer_expenditure as ce
import local_currency_mean as lcm

import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

path = os.path.dirname(__file__)
font_path = '\\\\'.join(path.split('\\'))+'\\\\font\\\\NanumGothic.ttf'
fontprop = fm.FontProperties(fname = font_path, size =10)

def covid_graph():
    yearly_data = co.covid_years()
    monthly_data = {k: yearly_data[k] for k in list(yearly_data.keys())[0:2]}
    fig = plt.figure(figsize=(12, 6))

    for i, (year, monthly_cases) in enumerate(monthly_data.items(),start=1):
        months = [data[0] for data in monthly_cases]
        cases = [data[1] for data in monthly_cases]

        ax = fig.add_subplot(1,2,i)  # 현재 subplot 가져오기
        bars = ax.bar(months, cases, color='skyblue')
        ax.tick_params(axis='x', rotation=45)

        # y축 눈금 설정
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

        # 각 막대 옆에 세 자리마다 컴마가 들어간 확진자 수 표시
        for bar in bars:
            formatted_case = "{:,}".format(bar.get_height())  # 세 자리마다 컴마 삽입
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), formatted_case,
                    ha='center', va='bottom', fontsize=5, color='black')
    fig.suptitle('경기도 코로나 확진자 수', fontproperties = fontprop)
    
    st.pyplot(fig)

def bsi():
    st.pyplot(BSI.get_bsi())

    
def emart_graph():
    yearly_data,data = emart.emart()
    yearly_data2 = yearly_data.iloc[[0,1]]
    data2 = data.loc[0:24]
    plt.figure(figsize=(12, 6))

    for i, year in enumerate(yearly_data2.index):
        plt.subplot(1, 2, i + 1)
        subset = data[data['년도'] == year]
        plt.plot(subset['월'], subset['매출액(단위:억원)'], marker='o')
        plt.title(f'E-mart Year {year} Sales')
        plt.xlabel('Month')
        plt.ylabel('Sales')

        # x축 눈금 설정
        plt.xticks(subset['월'])

    st.pyplot(plt)


def consumer_graph():
    ce.spend()
    
def local_mean_graph():
    st.pyplot(lcm.lcy())


