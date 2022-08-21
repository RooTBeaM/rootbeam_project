# Dataframe and arry
import numpy as np
import pandas as pd

# Historical data from binance
from binance.client import Client

# convert timestamp to Data and Time convert (UTC)
from datetime import datetime, date
import time 

# Plot Graph
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

import seaborn as sns
import mplfinance as mpf

# import file
from keys import API_key,Secret_key

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './function')
from setting import *
from indicators import *


# Check Binance Status
client = Client(API_key, Secret_key)
status = client.get_system_status()
print(status)

# df = get_kline('BTCUSDT', '4h', '1y')
def get_kline(symbol, tf, period): 
    klines = client.get_historical_klines(symbol, tf, period_dic[period])
    df = prepare_data(klines)
    return df

# df = get_kline_by_period('BTCUSDT', tf_dict['1d'], '2021-3', 'today')
def get_kline_by_period(symbol, tf, start, end):
    klines = client.get_historical_klines(symbol, tf, start, end)
    df = prepare_data(klines)
    return df
    
def prepare_data(klines):
    data = pd.DataFrame(klines, columns=row_col)
    data['OpenTime'] = pd.to_datetime(data['OpenTime'], unit='ms').dt.tz_localize('Asia/Bangkok')
    data['CloseTime'] = pd.to_datetime(data['CloseTime'], unit='ms').dt.tz_localize('Asia/Bangkok')
    df = data[['Open','High','Low','Close','Volume','QuoteAssetVol','TakerbaseVol','TakerquoteVol']].astype(float)
    df.set_index(data['OpenTime'], inplace=True)
    return df

def plotgraph(x,y):
    plt.figure(figsize=(30,5))
    plt.plot(x,y,linewidth=1, color='black')
    plt.xticks(rotation=65)
    plt.show()

####### test #####

df = get_kline_by_period('BTCUSDT', '4h', '2021-1', 'today')
plotgraph(df.index,df.Close)
df.to_csv("BTCUSDT.csv")