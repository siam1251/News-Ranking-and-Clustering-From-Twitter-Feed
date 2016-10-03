from Tweet import Tweet
from TwitterAccount import TwitterAccount
from TwitterData import TwitterData


class TweetFiles:
    __save_location = 'data'
    __end_delimiter ='end\n'

    def __init__(self):
        account = TwitterAccount()
        self.__api = account.get_api()

    def write_tweets(self, screen_name, update_count):
        since_time = TwitterData.since
        until_time = TwitterData.until
        print('Fetching data from %s ..........'%screen_name)
        # make initial request for most recent tweets
        try:
            alltweets = self.__api.user_timeline(screen_name=screen_name, since=since_time, until=until_time)
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
            tweet = Tweet(t.id_str, str(t.retweet_count), str(t.favorite_count),
                          str(t.created_at), t.text)
            f.write('%s \n'%str(tweet))
        f.write(self.__end_delimiter)
        f.close()

    def __delete_oldest_fetch(self, screen_name):
        lines = open('%s/%s.txt' % (self.__save_location, screen_name), 'r').readlines()
        for i in range(len(lines)):
            if lines[i] == self.__end_delimiter:
                break
        lines = lines[i+1:]
        open('%s/%s.txt' % (self.__save_location, screen_name), 'w').writelines(lines)

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

