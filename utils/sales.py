# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:30:11 2023

@author: rnjsd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import os

font_p = os.path.dirname(__file__)
font_path = '\\\\'.join(font_p.split('\\'))+'\\\\font\\\\NanumGothic.ttf'
fontprop = fm.FontProperties(fname = font_path, size =10)

file_p = os.path.dirname(__file__)
file_path = '\\\\'.join(file_p.split('\\'))+'\\\\row_data'
df_sales = pd.read_csv(file_path+'\\\\골목발달상권_추정매출(2020년).csv', encoding='euc-kr')
df2_sales = df_sales.copy()
sums1 = 0
sums2 = 0
result_list = []
for i in range(1,5):
    new_df2_sales = df2_sales[(df2_sales['기준분기'] == i)]
    sums1 = new_df2_sales['매출금액'].sum()
    sums2 = new_df2_sales['매출건수'].sum()
    if len(new_df2_sales['기준연도'].values) > 0:
        result_list.append({'기준연도':new_df2_sales['기준연도'].values[0], '기준분기':i, '매출금액':sums1, '매출건수':sums2})
result_df = pd.DataFrame(result_list)
def sales():
    fig = plt.figure(figsize=(15,6))
    ax1 = fig.add_subplot(1,1,1)
    ax2 = ax1.twinx()

    ax1.plot(result_df['기준분기'], result_df['매출금액'], color='r',label='매출금액')
    ax2.plot(result_df['기준분기'], result_df['매출건수'], color='b',label='매출건수')
    ax1.legend(loc='upper left', prop=fontprop)
    ax2.legend(loc='upper left', prop=fontprop, bbox_to_anchor=(0.0, 0.95))
    ax1.set_xticks(result_df['기준분기'])
    ax1.set_xlabel('분기', fontproperties=fontprop)
    ax1.set_ylabel('매출금액', fontproperties=fontprop, rotation=0)
    ax2.set_ylabel('매출건수', fontproperties=fontprop, rotation=0)
    fig.suptitle(f"{result_df['기준연도'][0]}년 골목발달상권", fontproperties=fontprop, size=20)
    return fig

