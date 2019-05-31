import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from datetime import datetime

def get_ticker():
    """
    It'll get the necessary info - ticker, startdate, enddate and will return a list of all these information
    """
    ticker = input("Enter ticker name: \n")
    start = input("Enter start date in this format: YYYY-M-D\n")
    end = input("Enter end date in this format: YYYY-M-D\n")
    stock_info = [ticker, start, end]
    return stock_info

def get_data(list):
    ticker = list[0]
    start = list[1]
    end = list[2]

    #Change the format of the dates to datetime format
    temp_start = start.split('-')
    start = datetime(int(temp_start[0]),int(temp_start[1]),int(temp_start[2]))
    temp_end = end.split('-')
    end = datetime(int(temp_end[0]),int(temp_end[1]),int(temp_end[2]))

    #I'll grab data from IEX in this case
    f = web.DataReader(ticker, 'iex', start, end)
    return f

def data_prep(df):
    """
    Adds the 50sma, 50sma_sd, sd_upper and sd_lower columns then returns the df w added info
    """
    df['sma50'] = df['close'].rolling(50,min_periods=1).mean() 
    df['sma50_sd'] = df['sma50'].rolling(50,min_periods=1).std()
    df['sd50_upper'] = df['sma50'] + 2*df['sma50_sd']
    df['sd50_lower'] = df['sma50'] - 2*df['sma50_sd']
    return df


if __name__ == '__main__':
    #get the data and returns as a df
    stock_list =get_ticker()
    f = get_data(stock_list)
    f = data_prep(f)
    #print(f.head())

    #plotting the data
        
    #convert the index to datetime:
    dates_times_obj = []
    for i in f.index:
        dates_times_obj.append(datetime.strptime(i, '%Y-%m-%d').date())
    #line graph
    plt.plot(dates_times_obj,f['close'])
    plt.plot(dates_times_obj,f['sma50'])
    plt.plot(dates_times_obj,f['sd50_upper'])
    plt.plot(dates_times_obj,f['sd50_lower'])
    plt.title('Time series of '+stock_list[0])
    plt.legend()
    plt.tight_layout()
    plt.show()

    