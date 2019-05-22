import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as style
import pandas as pd
import pandas_datareader.data as web   


plt.style.use('ggplot')    #style of plotting, as a default
start= dt.datetime(2017,1,1)
end = dt.datetime(2017,12,31)
df = web.DataReader('TSLA','iex', start, end)    #source = where we get it from
#df['sma_50'] = df['close'].rolling(window=50, min_periods=0).mean()
#df['sma_100'] = df['close'].rolling(window=100,min_periods=0).mean()
index = pd.to_datetime(df.index)    #convert to datetime format
df.index = index
#print(df.head())
#print(df.loc['2017-06-06'])


df_ohlc = df['close'].resample('7D').ohlc()
df_ohlc.reset_index(inplace=True)
#df_volume = df['volume'].resample('7D').sum()

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

df_ohlc['date'] = df_ohlc['date'].map(mdates.date2num)
print(df_ohlc.shape)

ax1 = plt.subplot2grid((1,1), (0,0))
candlestick_ohlc(ax1, df_ohlc)
