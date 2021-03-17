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

def getData(i):
    today=str(dt.datetime.now().strftime("%x"))
    today = today.replace('/','-')
    #labels
    PriceDf= price.createLabels(i)

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
                
                if Sentiment[1]==News[0]:
                    try:

                        
                        News[1]=np.asarray(News[1])
                        News[1]=np.squeeze(News[1])
                        Sentiment[0]=np.squeeze(Sentiment[0])
                        for Label in PriceList:
                            if News[0]==Label[1]:
                                input1.append(Sentiment[0])
                                input2.append(News[1])
                                labels.append(Label[0]) 
                                
                    except:
                        print(News[1])
                        print(Sentiment[0])
                        print(Label[0])
                        break

    return input1,input2,labels


def getPredictionData():
    Sentiment=[]
    News=[]
    predictionDay = (dt.date.today()-dt.timedelta(1)).isoformat()

    for filename in os.listdir('../FYP/TweetModel/TweetFolder/'):
        if filename.endswith(f'{predictionDay}-News.csv'):
            with open(f'../FYP/TweetModel/TweetFolder/{filename}', 'rb') as f:
                for line in f:
                    News.append(line.rstrip())

        if filename.endswith(f'{predictionDay}Tweet.csv'):
            with open(f'../FYP/TweetModel/TweetFolder/{filename}', 'rb') as f:
                for line in f:
                    Sentiment.append(line.rstrip())


    return Sentiment, News


def PredictionData(Sentiment, News):
    
    split=int(len(Sentiment)/10)
    drops=(len(Sentiment)%10)
    del Sentiment[(len(Sentiment)-drops):len(Sentiment)]
    Sentiment=np.asarray(Sentiment)
    Sentiment = np.split(Sentiment,split)
    News=[News]*split
    return Sentiment, News
    

def Predict(PredictionSentiments, PredictionNews, Model):
    pos=0
    neg=0
    neu=0

    PredictionSentiments=np.asarray(PredictionSentiments).astype('float32')
    PredictionNews=np.asarray(PredictionNews).astype('float32')

    for i in range(len(PredictionSentiments)):

        Sentiment=PredictionSentiments[i]
        News=PredictionNews[i]
        np.reshape(Sentiment,newshape=[1,10])
        np.reshape(News, newshape=[1,10])


        


        News = np.squeeze(News)
        Sentiment = np.squeeze(Sentiment)
        News = np.reshape(News,[1,10])
        Sentiment = np.reshape(Sentiment,[1,10])
        var = Model.predict({'I1':Sentiment,'I2':News})
        print(f'Prediction: {var}')

        if var>0.55:
            pos+=1
        elif var<0.45:
            neg+=1
        else:
            neu+=1

    
    print(f'pos: {pos}')
    print(f'neg: {neg}')
    print(f'neu: {neu}')

    return pos,neg,neu
