# author sayem.siam
# date: October 3, 2016
# This class is responsible to manage different news agencis
# and store the tweets in text files using another class Tweet files

from TweetFiles import TweetFiles

class NewsPapers:
    __news_paper_list = []

    def __init__(self):
        self.__tweet_files = TweetFiles()

    # use TweetFiles object to write all tweets in the text files
    def update_all_tweets(self,n_tweets, update_count, since, until):
        for screen_name in self.__news_paper_list:
            self.__tweet_files.write_tweets(screen_name, update_count, since, until)

    # use TweetFies object to read all the tweets from text files and
    # return the list of all tweets
    def get_all_tweets(self):
        all_tweets = []
        for screen_name in self.__news_paper_list:
            tweets = self.__tweet_files.read_tweets(screen_name)
            if tweets is not None and len(tweets) > 0:
                all_tweets.extend(tweets)

        return all_tweets

    # add a new news agency name to the list
    def add_news_paper(self, screen_name):
        self.__news_paper_list.append(screen_name)