import numpy as np
# Tachnical Analysis
import ta
# Libraries for fingding peak
from scipy.signal import find_peaks
from scipy.signal import argrelextrema

# This functions are modified for 

####################
# Trend indicators #
####################

def sma(df, window=13, fillna=False):
    indicator_sma = ta.trend.SMAIndicator(close=df['Close'], window=window, fillna=fillna)
    df[f"trend_sma_{window}"] = indicator_sma.sma_indicator()

def ema(df, window=13, fillna=False):
    indicator_ema = ta.trend.EMAIndicator(close=df['Close'], window=window, fillna=fillna)
    df[f"trend_ema_{window}"] = indicator_ema.ema_indicator()
    
# Average Directional Movement Index (ADX)
def adx(df, window=13, fillna=False):
    indicator_adx = ta.trend.ADXIndicator(high=df['High'], low=df['Low'], close=df['Close'], window=window, fillna=fillna)
    df['trend_adx'] = indicator_adx.adx()
    df['trend_adx_pos'] = indicator_adx.adx_pos()
    df['trend_adx_neg'] = indicator_adx.adx_neg()
    
# Aroon Indicator
def aroon(df, window=13, fillna=False):
    indicator_aroon = ta.trend.AroonIndicator(close=df['Close'], window=window, fillna=fillna)
    df['trend_aroon_up'] = indicator_aroon.aroon_up()
    df['trend_aroon_down'] = indicator_aroon.aroon_down()
    df['trend_aroon_ind'] = indicator_aroon.aroon_indicator()
    
# MACD
def macd(df, window_fast=13, window_slow=26, window_sign=9, fillna=False):
    indicator_macd = ta.trend.MACD(close=df['Close'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign, fillna=fillna)
    df['trend_macd'] = indicator_macd.macd()
    df['trend_macd_signal'] = indicator_macd.macd_signal()
    df['trend_macd_diff'] = indicator_macd.macd_diff()
    
# Mass Index
def mass_index(df, window_fast=9, window_slow=25, fillna=False):
    df['trend_mass_index'] = ta.trend.MassIndex(high=df['High'], low=df['Low'], window_fast=window_fast, window_slow=window_slow, fillna=fillna).mass_index()
    
# KST Indicator
def kst(df, fillna=False):
    indicator_kst = ta.trend.KSTIndicator(close=df['Close'], roc1=10, roc2=15, roc3=20, roc4=30, window1=10, window2=10, window3=10, window4=15, nsig=9, fillna=fillna)
    df['trend_kst'] = indicator_kst.kst()
    df['trend_kst_sig'] = indicator_kst.kst_sig()
    df['trend_kst_diff'] = indicator_kst.kst_diff()

# Schaff Trend Cycle (STC)
def stc(df, fillna=False):
    df['trend_stc'] = ta.trend.STCIndicator(close=df['Close'], window_slow=50, window_fast=23, cycle=10, smooth1=3, smooth2=3, fillna=fillna).stc()

#######################
# Momentam indicators #
#######################

# Relative Strength Index (RSI)
def rsi(df, window=14, fillna=False):
    df['momentum_rsi'] = ta.momentum.RSIIndicator(close=df['Close'], window=window, fillna=fillna).rsi()

# Stoch Indicator
def stoch(df, window=14,  smooth_window=3, fillna=False):
    indicator_so = ta.momentum.StochasticOscillator(high=df['High'], low=df['Low'], close=df['Close'], window=window, smooth_window=smooth_window, fillna=fillna)
    df['momentum_stoch'] = indicator_so.stoch()
    df['momentum_stoch_signal'] = indicator_so.stoch_signal()
    
# Rate Of Change
def roc(df, window=14, fillna=False):
    df['momentum_roc'] = ta.momentum.ROCIndicator(close=df['Close'], window=window, fillna=fillna).roc()
    
# Percentage Price Oscillator
def ppo(df, window_fast=13, window_slow=26, window_sign=9, fillna=False):
    indicator_ppo = ta.momentum.PercentagePriceOscillator(close=df['Close'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign, fillna=fillna)
    df['momentum_ppo'] = indicator_ppo.ppo()
    df['momentum_ppo_signal'] = indicator_ppo.ppo_signal()
    df['momentum_ppo_hist'] = indicator_ppo.ppo_hist()

#####################
# Volume indicators #
#####################

# On Balance Volume
def obv(df, fillna=False):
    df['volume_obv'] = ta.volume.OnBalanceVolumeIndicator(close=df['Close'], volume=df['Volume'], fillna=fillna).on_balance_volume()

# Force Index
def forceindex(df, window=13, fillna=False):
    df['volume_fi'] = ta.volume.ForceIndexIndicator(close=df['Close'], volume=df['Volume'], window=window, fillna=fillna).force_index()

#########################
# Volatility indicators #
#########################

# Average True Range
def atr(df, window=10, fillna=False):
    df['volatility_atr'] = ta.volatility.AverageTrueRange(close=df['Close'], high=df['High'], low=df['Low'], window=window, fillna=fillna).average_true_range()

# Bollinger Bands
def bollinger(df, window=20, window_dev=2, fillna=False):
    indicator_bb = ta.volatility.BollingerBands(close=df['Close'], window=window, window_dev=window_dev, fillna=fillna)
    df['volatility_bbm'] = indicator_bb.bollinger_mavg()
    df['volatility_bbh'] = indicator_bb.bollinger_hband()
    df['volatility_bbl'] = indicator_bb.bollinger_lband()
    df['volatility_bbw'] = indicator_bb.bollinger_wband()
    df['volatility_bbp'] = indicator_bb.bollinger_pband()
    df['volatility_bbhi'] = indicator_bb.bollinger_hband_indicator()
    df['volatility_bbli'] = indicator_bb.bollinger_lband_indicator()

# Donchian Channel
def bollinger(df, window=20, offset=0, fillna=False):
    indicator_dc = ta.volatility.DonchianChannel(high=df['High'], low=df['Low'], close=df['Close'], window=window, offset=offset, fillna=fillna)
    df['volatility_dcl'] = indicator_dc.donchian_channel_lband()
    df['volatility_dch'] = indicator_dc.donchian_channel_hband()
    df['volatility_dcm'] = indicator_dc.donchian_channel_mband()
    df['volatility_dcw'] = indicator_dc.donchian_channel_wband()
    df['volatility_dcp'] = indicator_dc.donchian_channel_pband()

######################
# Library form scipy #
######################

# Find Min-Max Peak 
def peak(df, sample=7):
    df['Close_min'] = df.iloc[argrelextrema(df['Close'].values, np.less_equal,order=sample)[0]]['Close']
    df['Close_max'] = df.iloc[argrelextrema(df['Close'].values, np.greater_equal,order=sample)[0]]['Close']
    df['High_min'] = df.iloc[argrelextrema(df['High'].values, np.less_equal,order=sample)[0]]['High']
    df['High_max'] = df.iloc[argrelextrema(df['High'].values, np.greater_equal,order=sample)[0]]['High']
    df['Low_min'] = df.iloc[argrelextrema(df['Low'].values, np.less_equal,order=sample)[0]]['Low']
    df['Low_max'] = df.iloc[argrelextrema(df['Low'].values, np.greater_equal,order=sample)[0]]['Low']

