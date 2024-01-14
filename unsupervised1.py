from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt

x, y = make_blobs(n_samples=100, n_features=2, random_state=12)
'''
    here n_sample means no. of rows, n_features means no. of column and random_state is used so we will get same rows 
    every time we run this code. 
'''
# print(x.shape)
x_train, x_test, y_train, y_test = train_test_split(x,y , test_size=0.33, random_state=12)

wcss = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, init='k-means++')
    kmeans.fit(x_train)
    wcss.append(kmeans.inertia_)
# print(wcss)

'''
--> Elbow Method:
The elbow method involves running the K-means algorithm for a range of values of n_clusters and plotting the WCSS 
(Within-Cluster Sum of Squares) against the number of clusters. The "elbow" in the plot represents a point where adding 
more clusters doesn't significantly reduce WCSS. The optimal number of clusters is often chosen at the elbow point.

>  KMeans clustering model is created with the specified number of clusters (n_clusters=k)
>  The init parameter in the KMeans constructor specifies the method used for initializing the cluster centroids before
    the iterative optimization process begins. The choice of initialization method can influence the convergence and 
    quality of the final clustering solution.
>  The inertia_ attribute of a fitted KMeans model contains the sum of squared distances of samples to their assigned 
    cluster centers. In other words, it represents the Within-Cluster Sum of Squares (WCSS) for the current clustering
     solution.
'''

# plt.plot(range(1,11),wcss)
# plt.xticks(range(1,11))
# plt.xlabel("Number of cluster")
# plt.ylabel("WCSS")
# plt.show()

# kmeans = KMeans(n_clusters=3, init='k-means++')
# y_label = kmeans.fit_predict(x_train)
# y_test_label = kmeans.predict(x_test)

# print(y_test_label)
# print(x_test[:0].shape, x_test[:0].shape)
# plt.scatter(x_train[:,0], x_train[:,1], c=y_label)
# plt.scatter(x_test[:,0], x_test[:,1], c=y_test_label)
# plt.show()

# k1 = KneeLocator(range(1,11), wcss, curve='convex', direction='decreasing')
# print(k1.elbow)
# '''it is used to directley find value of n_clusters'''