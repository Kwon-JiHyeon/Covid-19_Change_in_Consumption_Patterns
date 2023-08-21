# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:10:57 2023

@author: rnjsd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib import colors as mcolors
import os
import streamlit as st

path = os.path.dirname(__file__)
font_path = '\\\\'.join(path.split('\\'))+'\\\\font\\\\NanumGothic.ttf'
fontprop = fm.FontProperties(fname = font_path, size =10)

file_path = path+'\\\\row_data\\\\'
df_local = pd.read_csv(file_path+'지역화폐발행및이용현황.csv', encoding='euc-kr')
df2_local = pd.DataFrame(columns=df_local.columns)

for name in set(df_local['시군명']):
    new_df_local = df_local[df_local['시군명'] == name] .sort_values('기준년월')
    df2_local = pd.concat([df2_local, new_df_local], ignore_index=True)
    
new_mean_df2_local = pd.DataFrame()   
for date in set(df2_local['기준년월']):
    new_df2_local = df2_local[df2_local['기준년월'] == date]
    mean_df2_local = pd.DataFrame(new_df2_local.mean()).transpose()
    mean_df2_local.index = [date]
    new_mean_df2_local = pd.concat([new_mean_df2_local, mean_df2_local])
    new_mean_df2_local.sort_index(inplace=True)
    
def lcy():
    colors = ['b','g','r']
    fig = plt.figure(figsize=(15,6))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
            
    for i, column in enumerate(new_mean_df2_local.columns):
        if column != '월별신규가입자수(명)':
            ax1.plot(new_mean_df2_local.index, new_mean_df2_local[column], color=colors[i], label=column)
        else:
            ax2.plot(new_mean_df2_local.index, new_mean_df2_local[column], color=colors[i], label=column)
    
    ax1.legend(loc='upper left', prop = fontprop)
    ax2.legend(loc='upper left', prop = fontprop)
    fig.suptitle('경기도 지역화폐 발행 및 이용 현황', fontproperties = fontprop, size=15)
    return fig
