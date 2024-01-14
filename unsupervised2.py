from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sci

iris = datasets.load_iris()
df = pd.DataFrame(iris.data)
df.columns = iris.feature_names
# print(df)

sc = StandardScaler()
x_sc = sc.fit_transform(df)
# print(x_sc.shape)#(150, 4)

pca = PCA(n_components=2)
pcs_sc = pca.fit_transform(x_sc)
# print(pcs_sc.shape)#(150, 2)
'''
    Principal Component Analysis (PCA) is a dimensionality reduction technique that is commonly used in machine learning
    and statistics. 
    changing dimensions involves modifying the representation of data points by either reducing or expanding the number 
    of features.
ex. :-
Income | Expenditure
-------|------------
 50000 | 30000
 60000 | 35000
 75000 | 40000
 90000 | 45000
 
  Principal Component
--------------------
       -1.5
       -0.5
        0.5
        1.5
'''
# plt.scatter(pcs_sc[:,0],pcs_sc[:,1])
# plt.show()

# sci.dendrogram(sci.linkage(pcs_sc,method='ward'))
# plt.show()

cls = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='ward')
cls.fit(pcs_sc)
print(cls.labels_)

# sco = []
# for k in range(2,11):
#     algo = AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward')
#     algo.fit(x_sc)
#     sco.append(silhouette_score(x_sc,algo.labels_))
''' silhouette_score: This is a metric used to calculate how well-separated clusters are in a clustering result. It 
    measures the quality of clustering, with values ranging from -1 to 1. A higher silhouette score indicates 
    better-defined clusters. '''
# plt.plot(range(2,11), sco)
# plt.show()