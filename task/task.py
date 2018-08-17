# -*-coding:utf-8-*-
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(pd.read_csv('Bitcoin.csv'))
df.rename(columns={'price': 'Bitcoin'}, inplace=True)

for data_name in os.listdir('data'):
    name = str(data_name.split('.')[0])
    # print(name)
    each_data = pd.DataFrame(pd.read_csv('data/' + data_name))
    df = pd.merge(df, each_data, how='outer')
    df.rename(columns={'price': name}, inplace=True)

df['date'] = df['date'].str.replace('年', '-')
df['date'] = df['date'].str.replace('月', '-')
df['date'] = df['date'].str.replace('日', '')
df['date'] = pd.to_datetime(df['date'])
df.set_index("date", inplace=True)
print(df.head())
print(df.shape)

df.plot()
plt.xlabel('date')
plt.ylabel('price(USD)')
plt.show()