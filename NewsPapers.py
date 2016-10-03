from TweetFiles import TweetFiles

class NewsPapers:
    __news_paper_list = []

    def __init__(self):
        self.__tweet_files = TweetFiles()

    def update_all_tweets(self,n_tweets, update_count):
        for screen_name in self.__news_paper_list:
            self.__tweet_files.write_tweets(screen_name, update_count)

    def get_all_tweets(self):
        all_tweets = []
        for screen_name in self.__news_paper_list:
            tweets = self.__tweet_files.read_tweets(screen_name)
            if tweets is not None and len(tweets) > 0:
                all_tweets.extend(tweets)

        return all_tweets

    def add_news_paper(self, screen_name):
        self.__news_paper_list.append(screen_name)