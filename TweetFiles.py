# author sayem.siam
# date: October 3, 2016
# This class is responsible to write down all the tweets in the text files
#


from Tweet import Tweet
from TwitterAccount import TwitterAccount
from TwitterData import TwitterData
import datetime


class TweetFiles:
    __save_location = 'data'
    __end_delimiter ='end\n'

    def __init__(self):
        account = TwitterAccount()
        self.__api = account.get_api()


    # take input as screen name
    # fetch 10 tweets and only write few of those which are created in the time interval
    def write_tweets(self, screen_name, update_count, since_time, until_time):
        print('Fetching data from %s ..........'%screen_name)
        # make initial request for most recent tweets
        try:
            alltweets = self.__api.user_timeline(screen_name=screen_name, count = 10)
            print(since_time, until_time)
        except Exception, e:
            print(str(e))
            return

        outtweets = []
        if update_count > TwitterData.store_limit:
            self.__delete_oldest_fetch(screen_name)
        f = open('%s/%s.txt' % (self.__save_location, screen_name), 'a')
        for t in alltweets:
            #print(t.text.encode("utf-8"))
            #print(t.entities["urls"])
            string_date = str(t.created_at)
            created_at_time = datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S")
            if created_at_time > since_time and created_at_time < until_time:
                tweet = Tweet(t.id_str, str(t.retweet_count), str(t.favorite_count),
                              str(t.created_at), t.text)
                f.write('%s \n'%str(tweet))
        f.write(self.__end_delimiter)
        f.close()


    # delete the oldes tweet
    # uses the end_delimiter to find which lines to be deleted
    def __delete_oldest_fetch(self, screen_name):
        lines = open('%s/%s.txt' % (self.__save_location, screen_name), 'r').readlines()
        for i in range(len(lines)):
            if lines[i] == self.__end_delimiter:
                break
        lines = lines[i+1:]
        open('%s/%s.txt' % (self.__save_location, screen_name), 'w').writelines(lines)

    # read tweets from the stored text files
    # then make list of tweet objects and returns
    def read_tweets(self,screen_name):
        try:
            f = open('%s/%s.txt' % (self.__save_location, screen_name), 'r')
        except Exception, e:
            print(str(e))
            return

        all_tweets = []
        for line in f:
            if line == self.__end_delimiter:
                continue
            words = line.split(Tweet.delimiter)
            tweet = Tweet(words[0], words[1], words[2], words[3], words[4] )
            all_tweets.append(tweet)
        return all_tweets

