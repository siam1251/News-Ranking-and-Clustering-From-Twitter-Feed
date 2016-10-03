# author sayem.siam
# date: October 3, 2016
# This class is responsible to update data and notify the subsciber that
# a update data is avaiable
#

import NewsPapers


class TwitterData:
    __observerlist = []
    __all_tweets = []
    n_tweets = 10
    store_limit = 6
    update_count = 0
    since = ''
    until = ''

    def __init__(self, news_papers):
        self.news_papers = news_papers
    #
    #nofify all the subscriber instances
    def nofify_all_users(self):
        all_tweets = self.news_papers.get_all_tweets()
        for obs in self.__observerlist:
            obs.update(all_tweets)


    def get_all_tweets(self):
        return self.news_papers.get_all_tweets()

    # register a new subscriber
    def register_observer(self,observer):
        self.__observerlist.append(observer)
    #
    # update the data
    # then call method notify to all the subscriber
    def update_tweets(self, since, until, update_count):

        self.news_papers.update_all_tweets(self.n_tweets, update_count, since, until)
        self.nofify_all_users()
    def get_state(self):
        pass
