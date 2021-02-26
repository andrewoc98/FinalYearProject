import pandas as pd
import os
import numpy as np
import sys
import datetime as dt
import tensorflow as tf
import model
import tflearn.model_selection as tf
def trainModel(model,inputs,labels):
    
    model.fit(x=inputs,y=labels,epochs=20, validation_split=0.2)
    model.save(filepath='../PredictionModel/PredictionModel.bin')
    print("I work")
    
def getData():

    #labels
    PriceDf= pd.read_csv('../TweetModel/TweetFolder/Price.csv')
    Pricedf = Pricedf.tolist()
    SentimentList=[]
    NewsList=[]

    #Sentiments
    for filename in os.listdir('../TweetModel/TweetFolder/'):
        if filename.endswith('Tweet.csv'):
            df = pd.read_csv(f'../TweetModel/TweetFolder/{filename}',header=None)
            df,splits= normaliseData(df)
            SentimentList.append([df,filename[:(len(filename)-9)]])
    
    #news
    for filename in os.listdir('../TweetModel/TweetFolder/'):
        if filename.endswith('News.csv'):
            df=pd.read_csv(f'../TweetModel/TweetFolder/{filename}',header=None)
            NewsList.append([df,filename[:(len(filename)-9)]])


    inputs,labels =ShapeData(SentimentList,NewsList,PriceDf,splits)
    return inputs,labels
    


def normaliseData(dataframe):
    dataframe=dataframe.values.tolist()
    splits=int(len(dataframe)/10)
    drops=(len(dataframe)%10)
    del dataframe[(len(dataframe)-drops):len(dataframe)]
    return np.split(dataframe,splits),splits



def ShapeData(SentimentList,NewsList,PriceList,numofarray):
    inputs=[]
    labels=[]
    #Allign Sentiments and news
    for Sentiment in SentimentList:
        for News in NewsList:
            if Sentiment[1]==NewsList[1] :
                NewsArr=[NewsList[0]]*numofarray
                inputs.append([Sentiment[0],NewsArr])
                break
        
        for Label in PriceList:
            if Sentiment[1]==PriceList[1]:
                labels.append([Label]*numofarray)
                break
            

    return inputs,labels