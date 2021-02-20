import tweepy as twp
import csv
import datetime as dt
import sys
#import BertModel 
from BertModel.src.app import sentence_prediction as predict



class MyStreamListener(twp.StreamListener):
    def on_status(self, status):
        
        tweet = status.text
        
        while "@" in tweet:
            tweet = self.removeUser(tweet)

        while "http" in tweet:
            tweet = self.removeLink(tweet)

        while "#" in tweet:
            tweet=self.HashTagToWord(tweet)
           
        
        if tweet[:3]=="RT ":
            tweet = self.removeRetweetTag(tweet)
    
        #names the csv file after the current date
        date = dt.datetime.now()
        date= date.strftime("%x")
        date=str(date)
        date=date.replace('/','-')
        string='TweetModel/TweetFolder/'+date+'.csv'

        #trys to add the tweet to the next line in the csv file
        try:
            with open(string,'a', newline='') as f:
                tweet=predict(str(tweet))
                print(tweet)
                thewriter = csv.writer(f)
                thewriter.writerow([tweet])

        #usually occurs when emojis are present in the tweet
        #or when custom fonts are used
        except UnicodeEncodeError:
            print("could not handle this tweet")
            print(tweet)

    #remover users @'s from the tweet text
    def removeUser(self, string):
        atindex=string.index('@')
        spaceindex=string.find(' ',atindex)
        substr=string[atindex:spaceindex]
        string=string.replace(substr,"")
        return string

    #removes any links that begin with http from the tweet text
    def removeLink(self, string):
        webindex=string.index('http')
        spaceindex=string.find(' ',webindex)
        substr=string[webindex:spaceindex]
        string=string.replace(substr,"")
        return string

    #removes retweet tag from tweet (RT at the start of the string)
    def removeRetweetTag(self, string):
        substr=string[:2]
        string=string.replace(substr,"",1)
        return string

    #Changes the has tag to a word
    def HashTagToWord(self, string):

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

