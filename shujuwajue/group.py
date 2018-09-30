import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def load_data(file_name):
    return pd.read_csv(file_name, encoding='gbk')


def set_datetime_index(data, format='%Y%m%d'):
    data['日期'] = pd.to_datetime(data['日期'], format=format)
    data.set_index('日期', inplace=True)


def group_data():
    data = load_data('data.csv')
    set_datetime_index(data, format='%Y%m%d')
    i = 0
    for name, group in data.groupby(data['台区标识']):
        i += 1
        del group['台区标识']
        group.to_csv('./group/' + str(name) + '.csv')
    print(f'分组成功，总共分为{i}组')


def plot(data):
    print('开始画图')
    data[['功率因数均值', '功率因数标准差', '线损']].plot(subplots=True, sharex=True, sharey=False)
    data[['三相不平衡均值', '三相不平衡标准差', '线损']].plot(subplots=True, sharex=True, sharey=False)
    data[['电压均值', '电压标准差', '线损']].plot(subplots=True, sharex=True, sharey=False)
    data[['电流均值', '电流方差', '线损']].plot(subplots=True, sharex=True, sharey=False)
    data[['负载率均值', '负载率标准差', '线损']].plot(subplots=True, sharex=True, sharey=False)
    plt.show()


def get_data_path_list():
    data_list = os.listdir('group')
    return data_list


def data_plot(data_path_list):
    for data_path in data_path_list:
        data = load_data('group/' + data_path)
        plot(data)


def linear_model():
    data = load_data('group/1651044.csv')

    data_full = data
    data_full_x = np.array(data_full.drop(['线损', '日期'], 1))
    data_full_y = np.array(data_full['线损'])
    clf = LinearRegression()
    clf.fit(data_full_x, data_full_y)
    print('整体效果', clf.score(data_full_x, data_full_y))

    data = data[['功率因数均值', '三相不平衡均值', '电压均值', '电流均值', '负载率均值', '线损']]
    x = np.array(data.drop(['线损'], 1))
    y = np.array(data['线损'])

    clf = LinearRegression()
    clf.fit(x, y)
    print('去除标准差和方差效果', clf.score(x, y))


if __name__ == '__main__':
    # group_data()
    # data_165 = load_data('group/1651044.csv')
    # set_datetime_index(data_165, format='%Y-%m-%d')
    # plot(data_165)
    linear_model()
