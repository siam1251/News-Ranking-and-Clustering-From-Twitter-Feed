# author sayem.siam
# date: October 3, 2016
# This class is responsible to find the best
# tweet based on the retweet and favorite counts

from Tweet import Tweet

class BestTweet:
    def __init__(self, all_tweets, clusters):
        self.all_tweets = all_tweets
        self.clusters = clusters

    def comparator(self,a):
        a_score = int(self.all_tweets[a].retweet_count)\
                  +int(self.all_tweets[a].favorite_count)

        return a_score

    # sorts the each cluster based on retweets and likes
    def get_best_tweet(self):
        best_tweets = []
        print(self.clusters)
        for c in self.clusters:
            mx_t = max(c,key=self.comparator)
            best_tweets.append(mx_t)
        indices = max(best_tweets, key=self.comparator)
        ret_tweets = [indices, self.comparator(indices)]

        return ret_tweets

# for testing purpose only
if __name__ == '__main__':
    lst = []

    t = Tweet('', '4', '5', '', '', 'At least one death in the U.S. has been linked to an apparent clown hoax')
    lst.append(t)
    t = Tweet('', '3', '1', '', '', 'The new range dhaka going est Virginia Sheriff\'s Department')
    lst.append(t)
    t = Tweet('', '3', '0', '', '', 'T south Los Angeles at the end of a car chase')
    lst.append(t)
    t = Tweet('', '0', '9', '', '', 'I went taxes for up to 18 years  ')
    lst.append(t)
    t = Tweet('', '1', '1', '', '', 'I go')
    lst.append(t)
    best_tweet = BestTweet(lst,2)

    print(best_tweet.get_best_tweets())