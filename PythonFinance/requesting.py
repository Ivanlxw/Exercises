#Scraping list
import bs4 as bs
import pickle
import requests

#Getting pricing data
import os
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from random import shuffle

def save_snp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text,"lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker[:-1])
    
    with open("sp500_tickers.pickle","wb") as f:        #writebytes
        pickle.dump(tickers,f)
    return tickers

def get_data(reload_sp500=False):
    if reload_sp500:
        tickers = save_snp500_tickers()
    else:
        with open("sp500_tickers.pickle","rb") as f:        #readbytes
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):         #check if this file exits in directory
        os.makedirs('stock_dfs')

    start = dt.datetime(2015,1,1)
    end = dt.datetime(2019,6,1)
    #print(tickers)

    for ticker in tickers[:200]:
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'iex', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('Already have {}'.format(ticker))

def compile_data():
    with open("sp500_tickers.pickle","rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()

    for count,ticker in enumerate(tickers[:200]):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('date',inplace=True)
        df.columns = ['open','high','low',ticker,'volume']

        if main_df.empty:
            main_df = df.drop(['open','high','low','volume'],axis=1)
        else:
            main_df = main_df.join(df[ticker],how='outer')

        if count % 10 ==0:
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_close.csv')



#Getting a list of all the companies
"""
tickers = save_snp500_tickers()
print(tickers)
"""

#Saving the list into a csv with prices
#get_data(reload_sp500=True)


#Adjusted close from all stocks and combine into 1 large dataframe
compile_data()