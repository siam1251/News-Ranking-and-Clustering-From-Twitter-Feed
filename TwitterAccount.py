# author sayem.siam
# date: October 3, 2016
# This class is responsible to keep the twitter user credentials
# and return the user specific api


import tweepy
import Tweet
class TwitterAccount:

    __consumer_key = "gddg"
    __consumer_secret = "dgd"
    __access_key = "df-fgd"
    __access_secret = "dfgdfg"
    __api = ''
    __save_location = ''
    __tweet_count = 10
    def __init__(self):

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        auth.set_access_token(self.__access_key, self.__access_secret)
        self.__api = tweepy.API(auth)

    def get_api(self):
        return self.__api
