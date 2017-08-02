# News-Ranking-and-Clustering-From-Twitter-Feed

Hot news from twitter feeds

You are given a list of important news agencies and their twitter feeds.
There are a lot of news there: some of them are urgent and important, some aren’t.
Your task is to analyze those feeds, recognize moments when something extraordinary happens and send these news to another module, which will send the news to the users using push notifications.


Itlaunchs every 10 minutes and download all new tweets (or use Twitter streams, but it’s more complicated)
store tweet texts and attributes into storage
	(Features: Likes, share, comments, reactions…)
group tweets about the same event into one cluster
	(Based on similar words, distance to a word)
recognize events that are hot, urgent and worthy to send notification to users (not more than 2 per day)
	(based on likes, share)
select the “best” tweet from every such cluster
	(which has more likes)
create file with results: (tweet URL, tweet text, tweet date and any additional information you found useful) for every such cluster

You can select any features you want to group and rank the tweets. Try to achieve the best quality you can. On one hand, we shouldn’t disturb users with useless news, on the other hand, if something really important takes place, we should inform users as fast as we can. So both parameters are important for quality: 1) selection accuracy; 2) latency, i.e. time difference between first tweet about this event and creating notification.

New York Times
https://twitter.com/nytimes
The Sun
https://twitter.com/thesunnewspaper
The Times
https://twitter.com/thetimes
The Associated Press
https://twitter.com/ap
CNN
https://twitter.com/cnn
BBC NEWS
https://twitter.com/bbcnews
CNET
https://twitter.com/cnet
MSN UK
https://twitter.com/msnuk
Telegraph
https://twitter.com/telegraph
USAToday
https://twitter.com/usatoday
Wall Street Journal
https://twitter.com/wsj
Washington Post
https://twitter.com/washingtonpost
Boston Globe
https://twitter.com/bostonglobe
NEWS.com.au
https://twitter.com/newscomauhq
Sky News
https://twitter.com/skynews
SFGate
https://twitter.com/sfgate
Al-Jazeera
https://twitter.com/ajenglish
Independent, UK
https://twitter.com/independent
Guardian.co.uk
https://twitter.com/guardian
LA Times
https://twitter.com/latimes
Reuters
https://twitter.com/reutersagency
ABC News
https://twitter.com/abc
Bloomberg
https://twitter.com/bloombergnews
Business Week
https://twitter.com/bw
Time
https://twitter.com/time

