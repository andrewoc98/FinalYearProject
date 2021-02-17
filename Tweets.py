import tweepy
import StreamListener as sl

consumer_key="iJ4GiApERtf3EnUyCZTvUYW2f"
consumer_secret="tOW0ahJ8Ms0jFtLQcPp8gwsHO9HrbbkoHxkanPe0y4QACboEZp"
access_token="1309206976195440646-MfPe8TKbzHHWYLOs2naZwESbbQBtT8"
access_token_secret="lPQfa5y84lnx564BkfHXoNvtDKMgEGztJeq693m1imozd"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

myStreamListener= sl.MyStreamListener()
myStream= tweepy.Stream(auth= api.auth, listener=myStreamListener)

myStream.filter(track=['DJIA','Dow Jones','The Dow','djia','the dow','dow jones'])