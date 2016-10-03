from BestTweet import BestTweet
from TextFeatures import TextFeatures
from Tweet import Tweet
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import fcluster

from matplotlib import pyplot as plt

class ProcessData:
    n_clusters = 2
    hierarchical_dist = 5
    sav_location = 'results'

    def update(self, all_tweets):
        self.__all_tweets = all_tweets
        clusters = self.__find_clusters(self.n_clusters)
        print('clusters..')
        print(clusters)
        self.__print_clustered_tweets(clusters)
        self.__write_clustered_tweets(clusters)
        self.__get_best_tweets(clusters, 2)

    def __get_best_tweets(self, clusters, n):
        print('Finding best tweets ..........')
        best_tweet = BestTweet(self.__all_tweets, clusters)
        ret_tweets = best_tweet.get_best_tweet()
        f = open('%s/best_tweets.txt'%self.sav_location, 'wb')
        f.write('score=%s |   %s | tweet_url=%s\n'%(ret_tweets[1],\
                            self.__all_tweets[ret_tweets[0]].text, self.__all_tweets[ret_tweets[0]].get_url()))
        f.close()
        print(ret_tweets)
        return ret_tweets
    def __send_user_tweet(self):
        pass
    def __find_clusters(self, n_clusters):
        print('Finding features ..........')
        self.all_tweets_features = TextFeatures(self.__all_tweets).get_features()
        n_dimesion = len(self.all_tweets_features[0])
        self.all_tweets_features = self.__reduce_dimension(n_dimesion // 2)
        #clusters = self.__get_clusters_Kmeans(n_clusters)
        print('Doing clustering ..........')
        clusters = self.__get_clusters_hierarchical(10)
        return clusters
        #print(self.clusters)

    def __write_clustered_tweets(self, clusters):
        f = open('%s/clustered_tweets.txt'%self.sav_location,'wb')
        for each_cluster in clusters:
            f.write('----new cluster ---\n')
            for index in each_cluster:
                f.write('%s\n'%self.__all_tweets[index].text)
        f.close()

    def __print_clustered_tweets(self, clusters):
        for each_cluster in clusters:
            print('----new cluster---')
            for index in each_cluster:
                print(self.__all_tweets[index].text)

    # show dendogram
    def __show_dendogram(self, Z):
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
        plt.show()
    # used pca to reduce the dimensions
    def __reduce_dimension(self, n_components):
        X = np.array(self.all_tweets_features)
        pca = PCA(n_components=n_components)
        pca.fit(X)
        features = pca.fit_transform(X)
        return features

    # used kmeans algorithm to cluster the data
    def __get_clusters_Kmeans(self, n_clusters):
        X = np.array(self.all_tweets_features)
        kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
        clusters = [[] for i in range(n_clusters)]
        for index in range(len(kmeans.labels_)):
            label = kmeans.labels_[index]
            clusters[label].append(index)
        return clusters
    # used hierarchical clustering
    def __get_clusters_hierarchical(self, max_d):
        X = np.array(self.all_tweets_features)
        Z = linkage(X, 'ward')
        print('features')
        print(X)
        print('distances')
        print(Z)
        self.__show_dendogram(Z)
        fc = fcluster(Z, 8, criterion='distance')
        n = len(fc)
        clusters = [[] for i in range(max(fc))]
        for index in range(n):
            label = fc[index]
            # fcluster starts labeling from 1 and we label from 0
            clusters[label-1].append(index)
        return clusters


# for unit testing purpose only
if __name__ == '__main__':
    lst = []

    t = Tweet('', '4', '5', '',  'At least one death in the U.S. has been linked to an apparent clown hoax')
    lst.append(t)
    t = Tweet('', '3', '1', '', 'The new range dhaka going est Virginia Sheriff\'s Department')
    lst.append(t)
    t = Tweet('', '3', '0', '',  'T south Los Angeles at the end of a car chase')
    lst.append(t)
    t = Tweet('', '0', '10', '',  'I went taxes for up to 18 years  ')
    lst.append(t)
    t = Tweet('', '1', '1', '',  'I go')
    lst.append(t)

    processdata = ProcessData()
    processdata.n_clusters = 2
    processdata.update(lst)

