import tweepy as twp
import datetime as dt
import csv
from BertModel.src.app import sentence_prediction
import TweetModel.Price
from PredictionModel import train,model

def getNews():
    consumer_key="iJ4GiApERtf3EnUyCZTvUYW2f"
    consumer_secret="tOW0ahJ8Ms0jFtLQcPp8gwsHO9HrbbkoHxkanPe0y4QACboEZp"
    access_token="1309206976195440646-MfPe8TKbzHHWYLOs2naZwESbbQBtT8"
    access_token_secret="lPQfa5y84lnx564BkfHXoNvtDKMgEGztJeq693m1imozd"

    auth = twp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api=twp.API(auth)

    Today= dt.date.today()

    newstweets = api.search(
                            q="news",
                            count=10, 
                            result_type='popular', 
                            lang='en', 
                            until=Today
                            )

    newsarr=[]
    for tweet in newstweets:
        tweet=tweet.text
        while "@" in tweet:
            tweet = removeUser(tweet)

        while "http" in tweet:
            tweet = removeLink(tweet)

        while "#" in tweet:
            tweet= HashTagToWord(tweet)
            
        
        if tweet[:3]=="RT ":
            tweet =removeRetweetTag(tweet)

        Today=str(Today).replace('/','-')
        string='TweetModel/TweetFolder/'+Today+'-News.csv'

        #trys to add the tweet to the next line in the csv file
        try:
            with open(string,'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([sentence_prediction(str(tweet))])

            #usually occurs when emojis are present in the tweet
            #or when custom fonts are used
        except UnicodeEncodeError:
            pass

    TweetModel.Price.getPrice()
    predictmodel= model.create_model()
    input1, input2, labels=train.getData()
    train.trainModel(predictmodel,input1,input2,labels)
    

#remover users @'s from the tweet text
def removeUser(string):
    atindex=string.index('@')
    spaceindex=string.find(' ',atindex)
    substr=string[atindex:spaceindex]
    string=string.replace(substr,"")
    return string

#removes any links that begin with http from the tweet text
def removeLink(string):
    webindex=string.index('http')
    spaceindex=string.find(' ',webindex)
    substr=string[webindex:spaceindex]
    string=string.replace(substr,"")
    return string

#removes retweet tag from tweet (RT at the start of the string)
def removeRetweetTag(string):
    substr=string[:2]
    string=string.replace(substr,"",1)
    return string

#Changes the has tag to a word
def HashTagToWord(string):

    AllCaps=True
    Hashin= string.index('#')
    spaceindex=string.find(' ',Hashin)
    substr=string[Hashin:spaceindex]
    Output =''

    #removes the # symobol and places a space in each instance of a captial letter
    for i in range(len(substr)):
        if ord(substr[i])<91 and ord(substr[i])>64:
            Output=Output+' '+substr[i]
        elif substr[i]=='#':
            continue
        else:
            Output=Output+substr[i]
            AllCaps=False

    #if the string is all caps we remove all spaces in the output 
    if AllCaps:
        Output=Output.replace(" ","")

    #Change the hash string in the original tweet to the new string    
    string = string.replace(substr, Output)
    
    return string
    

    
