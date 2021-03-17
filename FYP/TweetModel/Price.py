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

    
def createLabels(days):
    df=pd.read_csv("../TweetModel/TweetFolder/Price.csv")
    df=df.values.tolist()
    output=[]
    i=0
    while i in range(len(df)) and i+days<len(df):
        if df[i][0]< df[i+days][0]:
            output.append([1,df[i][1]])
        else:
            output.append([0,df[i][1]])
        i+=1
    return output

