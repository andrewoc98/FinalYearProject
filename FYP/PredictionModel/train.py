import pandas as pd
import os
import numpy as np
import sys
import datetime as dt
import tensorflow as tf
def trainModel(model,input1,input2,labels):
    input1=np.asarray(input1).astype('float32')
    input2=np.asarray(input2).astype('float32')
    labels=np.asarray(labels).astype('float32')
    
    model.fit({'I1':input1,'I2':input2},labels,epochs=20, validation_split=0.2,verbose =1)
    model.save(filepath='../FYP/PredictionModel/PredictionModel.bin')
    print("I work")
    
def getData():
    today=str(dt.datetime.now().strftime("%x"))
    today = today.replace('/','-')
    #labels
    PriceDf= pd.read_csv('../FYP/TweetModel/TweetFolder/Price.csv')
    PriceDf = PriceDf.values.tolist()
    SentimentList=[]
    NewsList=[]

    #Sentiments
    for filename in os.listdir('../FYP/TweetModel/TweetFolder/'):
        if filename.endswith('Tweet.csv'):
            if(filename !=f'{today}Tweet.csv'):
                df = pd.read_csv(f'../FYP/TweetModel/TweetFolder/{filename}',header=None)
                df= normaliseData(str(filename[:(len(filename)-9)]),df)
                SentimentList.append(df)
                

    
    #news
    for filename in os.listdir('../FYP/TweetModel/TweetFolder/'):
        if filename.endswith('News.csv'):
            if(filename !=f'{dt.date.today().isoformat()}News.csv'):
                df=pd.read_csv(f'../FYP/TweetModel/TweetFolder/{filename}',header=None)
                NewsList.append([filename[:(len(filename)-9)],df])


    
    input1,input2,labels =ShapeData(SentimentList,NewsList,PriceDf)
    return input1,input2,labels
    


def normaliseData(Date,dataframe):
    output=[]
    dataframe=dataframe.values.tolist()
    splits=int(len(dataframe)/10)
    drops=(len(dataframe)%10)
    del dataframe[(len(dataframe)-drops):len(dataframe)]
    dataframe=np.asarray(dataframe)
    dataframe = np.split(dataframe,splits)
    for Sentiment in dataframe:
        output.append([Sentiment,Date])
    return output





def ShapeData(SentimentList,NewsList,PriceList):
    input1=[]
    input2=[]
    labels=[]
    
    #Allign Sentiments and news
    for News in NewsList:
        News[1]=News[1].values.tolist()
        for File in SentimentList:
            for Sentiment in File:
                NewsDate=DateConvert(News[0])
                if str(Sentiment[1])==NewsDate :
                    try:

                        
                        News[1]=np.asarray(News[1])
                        News[1]=np.squeeze(News[1])
                        Sentiment[0]=np.squeeze(Sentiment[0])
                        News[1]=News[1].tolist()
                        Sentiment[0]=Sentiment[0].tolist()
                        input1.append(Sentiment[0])
                        input2.append(News[1])
                        for Label in PriceList:
                            if News[0]==Label[1]:
                                labels.append(Label[2]) 
                                
                    except:
                        print(News[1])
                        print(Sentiment[0])
                        print(Label[2])
                        break

    return input1,input2,labels


def DateConvert(Date):
    Date=str(Date)
    Date=Date[2:]
    Date=Date[:-3]+'-'+Date[-2:]
    Date=Date[3:]+'-'+Date[:2]
    return Date
