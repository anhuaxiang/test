import datetime
import math
import time
import pickle

import matplotlib.pyplot as plt
import numpy as np
import quandl
from matplotlib import style
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

style.use('ggplot')


df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df.fillna(-9999, inplace=True)
open = "Adj. Open"
high = "Adj. High"
low = "Adj. Low"
close = "Adj. Close"
Volume = "Adj. Volume"
df = df[[open, high, low, close, Volume]]
forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

df['label'] = df[close].shift(-forecast_out)
df.dropna(inplace=True)
x = np.array(df.drop(['label'], 1))
y = np.array(df['label'])
x = preprocessing.scale(x)

x = x[:-forecast_out]
y = y[:-forecast_out]
x_lately = x[-forecast_out:]


print(len(x), len(y))

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
clf = LinearRegression()
clf.fit(x_train, y_train)
# print clf.predict(x_test)
accuracy = clf.score(x_test, y_test)
forecast_set = clf.predict(x_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
one_day = 86400 #Seconds in a day
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df[close].plot()
df["Forecast"].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
