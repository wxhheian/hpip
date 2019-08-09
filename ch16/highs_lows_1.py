import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  #reader阅读器对象
    header_row = next(reader)

    # for index,colunm_header in enumerate(header_row):             #index为索引
    #     print(index,colunm_header)

    #print(header_row)        #打印第一行

    #从文中获取最高气温
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
