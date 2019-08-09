import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)          #实参s设置了绘制图形时使用的点的尺寸   #c='yellow'
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

#设置图表标题并给坐标加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

#plt.show()

#自动将图表保存在文件中
plt.savefig('squares_plot.png',bbox_inches='tight')   #第二个参数将图片多余的空白区域剪掉
