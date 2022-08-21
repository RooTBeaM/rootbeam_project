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
from function.setting import *
from function.indicators import *

###################  Start form here #############

df = pd.read_csv("BTCUSDT.csv")

# EMA
ema(df, window=13)
ema(df, window=26)
ema(df, window=100)

#sma
sma(df, window=8)
sma(df, window=100)

#adx
adx(df, window=18)
aroon(df)
macd(df)
mass_index(df)
kst(df)
stc(df)

rsi(df)
stoch(df)
roc(df)
ppo(df)

obv(df)
forceindex(df)

atr(df)
bollinger(df)
Donchian(df)

peak(df)
print(df.tail())
df.to_csv("BTCUSDT_addInd.csv")