import tweepy as twp
import datetime as dt
from StreamListener import *


consumer_key="iJ4GiApERtf3EnUyCZTvUYW2f"
consumer_secret="tOW0ahJ8Ms0jFtLQcPp8gwsHO9HrbbkoHxkanPe0y4QACboEZp"
access_token="1309206976195440646-MfPe8TKbzHHWYLOs2naZwESbbQBtT8"
access_token_secret="lPQfa5y84lnx564BkfHXoNvtDKMgEGztJeq693m1imozd"

auth = twp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=twp.API(auth)

Today= dt.date.today()
#Yesterday= Today - datetime.timedelta(days=1)

newstweets = api.search(
                        q="news",
                        count=10, 
                        result_type='popular', 
                        lang='en', 
                        until=Today
                        )
def removeLink(string):
    webindex=string.index('http')
    spaceindex=string.find(' ',webindex)
    substr=string[webindex:spaceindex]
    string=string.replace(substr,"")
    return string

newsarr=[]
for tweet in newstweets:
    tweet=tweet.text
    print(tweet)
    if 'http' in tweet:
        tweet=removeLink(tweet)
    

    Today=str(Today).replace('/','-')
    string='TweetFolder/'+Today+'-News.csv'

    #trys to add the tweet to the next line in the csv file
    try:
        with open(string,'a', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow([str(tweet)])

        #usually occurs when emojis are present in the tweet
        #or when custom fonts are used
    except UnicodeEncodeError:
        print("could not handle this tweet")
        print(tweet)
    


