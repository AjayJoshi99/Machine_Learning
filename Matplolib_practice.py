import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.image as mpimg
import numpy as np
days = [1,2,3,4,5,6,7,8,9,4]
day_temp = np.random.randint(14,28,(10))
night_temp = np.random.randint(14,28,(10))
'''
# Line Graph
style.use('ggplot')
plt.plot(days,day_temp,label ='day temp',color='y',marker='o',markersize=10,linestyle='--',linewidth=4)
plt.plot(days,night_temp,label ='night temp',color='g',marker='o',markersize=10,linestyle='--',linewidth=4)
plt.title('Tempareture in winter', fontsize=15)
plt.xlabel('Temp', fontsize=13)
plt.ylabel('days', fontsize=13)
plt.grid(color = 'w',linestyle='-',linewidth=2)
plt.legend()
plt.show()
'''
'''
plt.hist([day_temp,night_temp],[14,16,18,20,22,24,26,28],rwidth=0.8,color=['g','k'],label=['Day temp','Night temp'])
plt.title('Tempareture in winter', fontsize=15)
plt.xlabel('Temp', fontsize=13)
plt.ylabel('days', fontsize=13)
plt.legend()
plt.show()
'''
'''
plt.figure(figsize=(8,6))
classes = ['ml', 'python', 'R','AI','DS']
c1 = [14,19,17,15,20]
c2 = [15,16,14,18,13]
c3 = [14,17,19,19,16]
class_index = np.arange(len(classes))#Creates an array of indices for the classes. This is used to position the bars on the x-axis.
width = 0.2
plt.bar(class_index,c1,width,color = 'g',label ='class1')
plt.bar(class_index+width,c2,width,color = 'k',label ='class2')
plt.bar(class_index+width+width,c3,width,color = 'm',label ='class3')
plt.xticks(class_index+width, classes)
plt.title('Students in class', fontsize=15)
plt.xlabel('class', fontsize=13)
plt.ylabel('students', fontsize=13)
plt.legend()
plt.show()
'''
'''
x = [1,3,5,2,5,6,7,2,5,6]
y = [5,3,1,6,7,8,5,3,2,9]
plt.scatter(x,y,label='None')
plt.title('Practice', fontsize=15)
plt.xlabel('x-axis', fontsize=13)
plt.ylabel('y-axis', fontsize=13)
plt.legend()
plt.show()
'''
'''
classes = ['ml', 'python', 'R','AI','DS']
c1 = [14,19,17,15,20]
explodes = [0.1,0.2,0,0,0]
colors = ['b','g','m','r','y']
font_size = {'fontsize': 13}
plt.pie(c1,labels= classes, explode = explodes, colors = colors,autopct='%1.1f%%', shadow=True, radius=1.4,
        textprops = font_size, startangle = 30)
plt.subplots_adjust(top=0.6)
plt.savefig("pie_chart",dpi=400)
'''
'''
plt.subplot(2,2,1)
plt.pie([1])
plt.subplot(2,2,2)
plt.pie([1,2])
plt.subplot(2,2,3)
plt.pie([1,2,3])
plt.subplot(2,2,4)
plt.pie([1,2,3,4])
plt.show()
'''
'''
plt.subplot(2,2,1)
style.use('ggplot')
plt.plot(days,day_temp,label ='day temp',color='y',marker='o',linestyle='--',linewidth=4)
plt.plot(days,night_temp,label ='night temp',color='g',marker='o',linestyle='--',linewidth=4)
plt.title('Tempareture in winter')
plt.xlabel('Temp')
plt.ylabel('days')
plt.grid(color = 'w',linestyle='-',linewidth=2)
plt.legend()


plt.subplot(2,2,2)
classes = ['ml', 'python', 'R','AI','DS']
c1 = [14,19,17,15,20]
c2 = [15,16,14,18,13]
c3 = [14,17,19,19,16]
class_index = np.arange(len(classes))#Creates an array of indices for the classes. This is used to position the bars on the x-axis.
width = 0.2
plt.bar(class_index,c1,width,color = 'g',label ='class1')
plt.bar(class_index+width,c2,width,color = 'k',label ='class2')
plt.bar(class_index+width+width,c3,width,color = 'm',label ='class3')
plt.xticks(class_index+width, classes)
plt.title('Students in class', fontsize=15)
plt.xlabel('class', fontsize=13)
plt.ylabel('students', fontsize=13)
plt.legend()

plt.subplot(2,2,3)
x = [1,3,5,2,5,6,7,2,5,6]
y = [5,3,1,6,7,8,5,3,2,9]
plt.scatter(x,y,label='None')
plt.title('Practice')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.subplot(2,2,4)
classes = ['ml', 'python', 'R','AI','DS']
c1 = [14,19,17,15,20]
explodes = [0.1,0.2,0,0,0]
colors = ['b','g','m','r','y']
plt.pie(c1,labels= classes, explode = explodes, colors = colors,autopct='%1.1f%%', shadow=True, radius=1.4,
         startangle = 30)
plt.subplots_adjust(top=0.6)
plt.title('Students in class')
plt.subplots_adjust(wspace=0.5, hspace=0.9)
plt.show()
'''
#
# img = mpimg.imread("C:\\Users\\Joshi Ajay\\Pictures\\Saved Pictures\\Wallpaper.jpg")
# img2 = img[:,:,1]
# plt.axis('off')
# plt.imshow(img2, cmap='hot')
# plt.show()