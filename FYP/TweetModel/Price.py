import bs4
import requests
from bs4 import BeautifulSoup
import csv
import datetime as dt


def getPrice():
    url=requests.get('https://finance.yahoo.com/quote/%5EDJI?p=^DJI&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(url.text, features='html.parser')
    price= soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    price = price.replace(',','')
    price = float(price)

    with open('../FYP/TweetModel/TweetFolder/Price.csv','a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([price,dt.date.today().isoformat()])

