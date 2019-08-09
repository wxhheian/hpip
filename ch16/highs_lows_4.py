import csv
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取日期，最高气温，最低气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)    #reader阅读器对象
    header_row = next(reader)       #csv文件的第一行对象

    dates,highs,lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)


#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)       #alpha指定颜色的透明度 1表示完全不透明 0便是完全透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
plt.title('Daily high and low temperatures - 2014, July 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()           #绘制斜的日期标签
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()
