# -*- coding: utf-8 -*-
"""
Created on Mon May 18 13:13:26 2020

@author: Okey
"""
import pandas as pd 
import pandas_datareader as pdr
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters

class Analyze:
    
    default_date = dt.date.isoformat(dt.date.today() - dt.timedelta(397))
    
    def get_data(symbol, date=default_date):
        data = pdr.get_data_yahoo(symbol, start=date)
        return data
    
        data = pdr.get_data_yahoo(symbol, start=date)
        return data
    
    def moving_avg(okey, fast=5, slow=20):
        okey[str(fast) + '_day'] = okey.Close.rolling(fast).mean()
        okey[str(slow) + '_day'] = okey.Close.rolling(slow).mean()
        
    def plot_MA(okey):
            okey['tradeSignal']=np.where(okey['5_day'] > okey['20_day'], 'buy', 'sell')
            plt.plot(okey['Close'])
            plt.plot(okey.fliter(regex='day'))
            plt.grid(True)

    
