from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

x, y = make_moons(n_samples=250, noise=0.05)
# print(x.shape)#(250, 2)
'''
noise: Controls the amount of random noise added to the data. In this case, the value is set to 0.05, which means that 
        5% of the data points will be randomly perturbed to introduce some variability.
Adding a small amount of noise can make the synthetic dataset more realistic and reflect the inherent variability often 
found in real-world data. It also allows for testing the robustness of clustering algorithms like DBSCAN to noisy data.
'''
sc = StandardScaler()
x_sc = sc.fit_transform(x)
dbscan = DBSCAN(eps=0.5)
'''
Certainly! In simple terms, the eps parameter in DBSCAN determines how far away points can be from each other and still 
    be considered part of the same group (cluster). It sets a limit on the distance within which points are considered 
    neighbors.

Imagine you have a bunch of points scattered on a plane. The eps value defines a distance around each point. If another 
    point falls within this distance from a given point, they are considered neighbors. If this happens for several 
    points, they form a cluster
'''

dbscan.fit(x_sc)
# print(dbscan.labels_)
# plt.scatter(x[:,0],x[:,1],c = y)
# plt.scatter(x[:,0],x[:,1],c = dbscan.labels_)
plt.show()