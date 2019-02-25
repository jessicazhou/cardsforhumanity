import urllib2
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
 

url = sys.argv[1]
url = "https://www.twitter.com/"+url
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
tweet_list = []

tweets = soup.find_all('li','js-stream-item')
for tweet in tweets:
    if tweet.find('p','tweet-text'):
        #tweet_user = tweet.find('span','username').text
        tweet_text = tweet.find('p','tweet-text').text.encode('utf8')
        #tweet_id = tweet['data-item-id']
        #timestamp = tweet.find('a','tweet-timestamp')['title']
        #tweet_timestamp = dt.datetime.strptime(timestamp, '%H:%M - %d %b %Y')
        tweet_list.append(text_text) #builds a list


#after the list is built
tfidf = TfidfVectorizer()

response=tfidf.fit_transform(tweet_list)
feature_names = tfidf.get_feature_names()
for col in response.nonzero()[1]:
    print(feature_names[col],' - ', response[0, col])