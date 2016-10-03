import tweepy
import Tweet
class TwitterAccount:

    __consumer_key = "sp27s8qtfeY835V31RIIUI4vp"
    __consumer_secret = "2aL695hSBEtSZ28jSmQpgBrYCY1354iVY4u7ieCfkRygxtV6Uw"
    __access_key = "163882382-YSNSn0LVaWNo7NvUcSsS1BpTQeyWAbqUpBvsK7tZ"
    __access_secret = "tLgP44Ae4PtvfU1lb9FsKPUvRJMdJQ8af7NoRRLOFXho8"
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