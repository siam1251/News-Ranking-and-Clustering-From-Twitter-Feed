# author sayem.siam
# date: October 3, 2016
# This class is responsible to keep the twitter user credentials
# and return the user specific api


import tweepy
import Tweet
class TwitterAccount:

    __consumer_key = "C0XgZpQR09rKElSPLPJCdXyaN"
    __consumer_secret = "vLnXuoxRboWai0ouYoLrUxQpBmkHrNhwSvSNsaFJjEgO4NKnQn"
    __access_key = "163882382-QyqXLMzulnfklXEKPBZtoy4On0a2SZaYXK645GLX"
    __access_secret = "tqkVjAAYwqXnDrLXNJtNNs03OUo9dbF45oSdVVyDMMZjy"
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