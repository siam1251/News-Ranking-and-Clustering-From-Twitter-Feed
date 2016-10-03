from NewsPapers import NewsPapers
from ProcessData import ProcessData
from TwitterData import TwitterData
import os.path
import datetime
import sys
import time

if __name__ == '__main__':
    sav_location = 'data'
    reload(sys)
    sys.setdefaultencoding('utf8')

    papers = ['nytimes', 'thesunnewspaper', 'ap', 'thetimes', 'cnn', 'bbcnews',\
              'bbcnews',  'cnet', 'msnuk', 'telegraph', 'usatoday', 'wsj', 'washingtonpost', 'newscomauhq'\
              'skynews', 'sfgate', 'ajenglish', 'independent', 'guardian', 'latimes', 'reutersagency', \
              'abc', 'bloombergnews', 'bw', 'time'
              ]
    # papers = ['nytimes']
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
    while(True):
        update_count+= 1

        now = datetime.datetime.now()
        f_name = '%s/since.txt'%sav_location
        # check if we know the time until we fetched
        if os.path.isfile(f_name):
            f = open(f_name)
            since_time = f.readlines().strip()
            f.close()
        else:
            # else we fetch from last 10 minutes
            since_time = now - datetime.timedelta(minutes=10)
            since = since_time.isoformat()
        until = now.isoformat()
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


