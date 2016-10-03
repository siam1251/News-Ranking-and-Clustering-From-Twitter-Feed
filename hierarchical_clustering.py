from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import fcluster

from matplotlib import pyplot as plt
for i in range(10):
    print(i)
print(i)

X = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
Z = linkage(X, 'ward')
c, coph_dists = cophenet(Z, pdist(X))
print(c)
print(Z)
# calculate full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
cluster = fcluster(Z, 1, criterion='distance')
print(cluster)
plt.show()