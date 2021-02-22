import bs4
import requests
from bs4 import BeautifulSoup
import csv
import datetime as dt
import pandas as pd


def getPrice():
    url=requests.get('https://finance.yahoo.com/quote/%5EDJI?p=^DJI&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(url.text, features='html.parser')
    price= soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    price = price.replace(',','')
    price = float(price)

    with open('../FYP/TweetModel/TweetFolder/Price.csv','a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([price,dt.date.today().isoformat()])

    createLabels()

def createLabels():

    df = pd.read_csv("../TweetModel/TweetFolder/Price.csv")
    PrevPrice=df['Price'].iloc[-2]
    CurrentPrice=df['Price'].iloc[-1]


    if PrevPrice>CurrentPrice:
        df['Label'].iloc[-2]=0
    elif PrevPrice<CurrentPrice:
        df['Label'].iloc[-2]=1
    else:
        df['Label'].iloc[-2]=0.5


    f = open('../TweetModel/TweetFolder/Price.csv', 'r+')
    f.truncate(0)
    df.to_csv("../TweetModel/TweetFolder/Price.csv", index=False)



