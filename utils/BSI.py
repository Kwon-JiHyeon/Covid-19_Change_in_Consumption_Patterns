# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 13:08:37 2023

@author: rnjsd
"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager
import os

file_p = os.path.dirname(__file__)
file_path = '\\\\'.join(file_p.split('\\'))+'\\\\row_data'
df = pd.read_csv(file_path+'\\소상공인시장진흥공단_소상공인 경기동향(BSI) 현황_20230730.csv', encoding='euc-kr')
df_trd = pd.read_csv(file_path+'\\소상공인시장진흥공단_전통시장 경기동향(BSI) 현황_20230730.csv', encoding='euc-kr')
df_copy = df.copy()
df['연월'] = df['연도'].astype(str)+ '.' + df['월'].astype(str)
df.set_index('연월', inplace=True)
df.drop(['연도', '월'], inplace=True, axis=1)
df2 = df.copy()
df3 = df2.loc['2019.9':'2021.3','경기체감':'경기전망']

df_trd_copy = df_trd.copy()
df_trd['연월'] = df_trd['연도'].astype(str)+ '.' + df_trd['월'].astype(str)
df_trd.set_index('연월', inplace=True)
df_trd.drop(['연도', '월'], inplace=True, axis=1)
df2_trd = df_trd.copy()
df3_trd = df2_trd.loc['2019.9':'2021.3','경기체감':'경기전망']

font_p = os.path.dirname(__file__)
font_path = '\\\\'.join(font_p.split('\\'))+'\\\\font\\\\NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname = font_path, size =10)
def get_bsi():
    fig = plt.figure(figsize=(15,6))
    ax = fig.add_subplot(1,1,1)
    ax.plot(df3['경기체감'].index, df3['경기체감'].values, color ='b',marker='o',label='소상공인')
    ax.plot(df3_trd['경기체감'].index, df3_trd['경기체감'].values, color ='r',marker='o',label='전통시장')
    ax.legend(loc='upper left', prop=fontprop)
    ax.set_title('경기도 소상공인, 전통시장 BSI', fontproperties = fontprop, size=20)
    ax.set_xlabel('날짜',fontproperties = fontprop, size=10)
    ax.set_ylabel('BSI', size=10, rotation=0)
    for i, value in enumerate(df3['경기체감'].values):
        ax.text(df3['경기체감'].index[i], value, str(value), ha='center', va='bottom')
    
    for i, value in enumerate(df3_trd['경기체감'].values):
        ax.text(df3_trd['경기체감'].index[i], value, str(value), ha='center', va='bottom')
    return fig

