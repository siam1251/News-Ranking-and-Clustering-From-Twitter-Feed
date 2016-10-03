from NewsPapers import NewsPapers
from ProcessData import ProcessData
from TwitterData import TwitterData
import os.path
import datetime
import sys
import time
import re

if __name__ == '__main__':
    sav_location = 'data'
    reload(sys)
    sys.setdefaultencoding('utf8')
    filelist = [f for f in os.listdir(sav_location) if f.endswith(".txt")]
    for f in filelist:
        os.remove(sav_location+'/'+f)

    papers = ['nytimes', 'thesunnewspaper', 'ap', 'thetimes', 'cnn', 'bbcnews',\
              'bbcnews',  'cnet', 'msnuk', 'telegraph', 'usatoday', 'wsj', 'washingtonpost',\
              'skynews', 'sfgate', 'ajenglish', 'independent', 'guardian', 'latimes', 'reutersagency', \
              'abc', 'bw', 'time'
              ]
    #papers = ['nytimes']
    news_papers = NewsPapers()
    for i in papers:
        print(i)
        news_papers.add_news_paper(i)
    # instantiate a new twitter data class with a newspapers instance
    twitter_data = TwitterData(news_papers)

    # it will cluster and find the best news tweet
    process_data = ProcessData()

    # register process data instance with the twitter data instance
    twitter_data.register_observer(process_data)

    update_count = 0
    #
    update_interval = 10*60 # 10 minutes
    twitter_data.store_limit = 6 # 6*10 = 60 minutes
    while(True):
        update_count+= 1

        now = datetime.datetime.utcnow()
        f_name = '%s/since.txt'%sav_location
        # check if we know the time until we fetched
        if os.path.isfile(f_name):
            f = open(f_name)
            since = f.readlines()[0].rstrip('\n')
            since = datetime.datetime.strptime(since, "%Y-%m-%d %H:%M:%S.%f")
            f.close()
        else:
            # else we fetch from last 10 minutes
            since = now - datetime.timedelta(minutes=60)

        until = now

        #updating with recent tweets
        twitter_data.update_tweets(since, until, update_count)
        tweets = twitter_data.get_all_tweets()
        # write the the time until we fetched
        f = open(f_name,'w')
        f.write('%s'%until)
        f.close()
        print('paused for %s seconds!'%update_interval)
        time.sleep(update_interval)
        # for t in tweets:
        #     print(str(t))


