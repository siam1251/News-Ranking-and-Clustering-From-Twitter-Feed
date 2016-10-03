# author sayem.siam
# date: October 3, 2016
# this is a subscriber class which can be registerd with the TwitterData object.
# the update method of this class is automatically called whenever TwitterData.update_tweets()
# method is called.
#
# This class is responsible to create clusters of the all tweets and return a tweet to users
# It creates three text files in the results folder



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
    hierarchical_dist = 3
    sav_location = 'results'
    thresh_score = 1

    # this method of this class is automatically called whenever TwitterData.update_tweets() is called
    # it calls the private method __find_clusters(self.n_clusters)
    # it also calls the private method to send user a notification
    def update(self, all_tweets):
        self.__all_tweets = all_tweets
        clusters = self.__find_clusters(self.n_clusters)
        if clusters is None:
            return
        print('clusters..')
        print(clusters)
        self.__send_user_tweet(clusters)
        self.__print_clustered_tweets(clusters)
        self.__write_clustered_tweets(clusters)

    # returns the best tweet
    def __get_best_tweets(self, clusters):
        print('Finding best tweets ..........')
        best_tweet = BestTweet(self.__all_tweets, clusters)
        ret_tweet = best_tweet.get_best_tweet()
        f = open('%s/best_tweets.txt'%self.sav_location, 'wb')
        f.write('score=%s |   %s | tweet_url=%s\n'%(ret_tweet[1],\
                            self.__all_tweets[ret_tweet[0]].text, self.__all_tweets[ret_tweet[0]].get_url()))
        f.close()
        print(ret_tweet)
        return ret_tweet

    # send user a notification if a best tweet has a score greater than a threshold
    # if there is a tweet in the send_user.txt file that means users will be notified
    def __send_user_tweet(self,clusters):
        ret_tweet = self.__get_best_tweets(clusters)
        f = open('%s/send_user.txt' % self.sav_location, 'w')
        if ret_tweet[1] > self.thresh_score:
            f.write('score=%s |   %s | tweet_url=%s\n' % (ret_tweet[1], \
            self.__all_tweets[ret_tweet[0]].text, self.__all_tweets[ret_tweet[0]].get_url()))
        f.close()
        pass

    # This method calls reduce dimension method to reduce the dimension of the feature space
    # I reduced the dimension by half
    # Then call hierarchical cluster method to cluster the data
    def __find_clusters(self, n_clusters):
        print('Finding features ..........')
        self.all_tweets_features = TextFeatures(self.__all_tweets).get_features()
        if len(self.all_tweets_features) < 1:
            print('No updated tweets found')
            return
        n_dimesion = len(self.all_tweets_features[0])
        self.all_tweets_features = self.__reduce_dimension(n_dimesion // 2)
        #clusters = self.__get_clusters_Kmeans(n_clusters)
        print('Doing clustering ..........')
        clusters = self.__get_clusters_hierarchical(self.hierarchical_dist)
        return clusters
        #print(self.clusters)

    # this method writes the cluster tweet text in the clustered_tweets.txt file
    def __write_clustered_tweets(self, clusters):
        f = open('%s/clustered_tweets.txt'%self.sav_location,'w')
        for each_cluster in clusters:
            f.write('             #################### new cluster ########################\n\n')
            for index in each_cluster:
                f.write('%s\n'%self.__all_tweets[index].text)
        f.close()

    # this method prints the clustered tweets
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

    # didn't use this method
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
        if len(X) < 2:
            print('There is only single news tweet')
            return
        Z = linkage(X, 'ward')
        print('features')
        print(X)
        print('distances')
        print(Z)
        #self.__show_dendogram(Z)
        fc = fcluster(Z, max_d, criterion='distance')
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

