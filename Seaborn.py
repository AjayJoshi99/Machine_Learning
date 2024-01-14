import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas import DataFrame
from matplotlib.pyplot import show,title,figure,legend
'''
days = np.arange(15)
temp = [23,32,34,43,19,20,35,36.5,32,30,38,31,28,40,20]
df = DataFrame({'days':days,'tempreture':temp})
sns.lineplot(y ="days",x="tempreture" ,data=df)
show()
'''

# figure(figsize=(16,9))
# sns.set(style='darkgrid')
# tips = sns.load_dataset("tips")#it imports dataset from github
# sns.lineplot(x="size", y = "total_bill", data=tips, hue="sex", palette="hot", style="sex", markers=["o","<"])
# title("Practice of seaborn")#palette is used for automatic colour combination
# #hue is used for divideing graph in to multiple graph
# #style is used for different line style for perticular type
# show()


# sns.set()
# tips = sns.load_dataset("tips")
# b = [1,5,10,15,20,25,30,35,40,50,55]#value of x-axis
# sns.displot(tips["total_bill"],label="Total Bill",bins=b,color='g',kde=True) #kde is used for line curve
# legend()#for label
# show()


# order = ['Sun', 'Thur','Fri','Sat']
# hue_order = ['Male','Female']
# kwargs = {'alpha':0.9, 'linestyle':"-",'linewidth':4,'edgecolor':'k'}
# ax = sns.barplot(x= 'day', y ='total_bill', hue='sex', data = tips, order = order,
#             hue_order=hue_order,errorbar=('ci', 100),
#             palette="hot",**kwargs)#dodge=False is used fpr overlapping
# ax.set(title ='Practice', xlabel='DAYS', ylabel='TOTAL_BILL')
# plt.savefig("seaborn_barplot")
# show()

# titanic = sns.load_dataset("titanic")
# sns.scatterplot(x='age', y = 'fare', data = titanic, hue='alive', style='who',size ='who',sizes=(80,100))
# show()


# plt.figure(figsize=(16,9))
# annot_kws= {'fontsize':7,
#             'fontstyle': 'italic',
#             'color': 'k',
#             'alpha': 0.6,
#             'backgroundcolor':'w'}
# global_w = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\Who_is_responsible_for_global_warming.csv")
# global_w = global_w.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'], axis=1).set_index('Country Name')
# ax = sns.heatmap(global_w, cmap='coolwarm', annot = True,annot_kws=annot_kws, linewidths=4,linecolor='k')
# ax.set(title='Heatmap practice for global warming dataset',
#        xlabel='CO2 emmision per year',
#        ylabel= 'Country Name')
# sns.set(font_scale=2)
# show()


plt.figure(figsize=(16,9))
annot_kws= {'fontsize':7,
            'fontstyle': 'italic',
            'color': 'k',
            'alpha': 0.6,
            'backgroundcolor':'w'}
global_w = pd.read_csv("C:\\Users\\Joshi Ajay\\Downloads\\Who_is_responsible_for_global_warming.csv")
global_w = global_w.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'], axis=1).set_index('Country Name')
ax = sns.heatmap(global_w.corr(), cmap='coolwarm', annot = True,annot_kws=annot_kws, linewidths=4,linecolor='k')
ax.set(title='Heatmap practice for global warming dataset',
       xlabel='CO2 emmision per year',
       ylabel= 'Country Name')
sns.set(font_scale=2)
show()

