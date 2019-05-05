#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:13:29 2019

@author: dh08loma
"""

import urllib
import requests
import pandas as pd
import json
import string

import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime



api_key='UUCHROXZD4ID2ZF2'
symbol='ACB'


#Alpha Vantage API
def plot_stock(symbol):
    #compact,full
    api_call_string='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&outputsize=compact'.format(symbol,'UUCHROXZD4ID2ZF2')        

    res=urllib.request.urlopen(api_call_string).read()
    data = json.loads(res.decode())
    
    
    ts_data=data['Time Series (Daily)']


    dates=np.flip([datetime.strptime(key, "%Y-%m-%d") for key in ts_data.keys()])
    
    closing_values=[float(ts_data[date.strftime("%Y-%m-%d")]['4. close']) for date in dates]
    
    
    stock_df=pd.DataFrame({'Date':dates,
                           'Value':closing_values})
    
    plt.plot(stock_df['Date'],stock_df.Value)
    plt.title(symbol+' price over time',fontsize=20)




plot_stock('ACB')





stocks_dict={'Stock':[],
             'Market':[],
             'Symbol':[],
             'Close':[]}

letters = list(string.ascii_uppercase)

for market in ['NASDAQ','NYSE']:
    for letter in letters:
        
        url='http://eoddata.com/stocklist/{}/{}.htm'.format(market,letter)

        #Get URL page 
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        tr_results=soup.find_all('tr')
        
        for result in tr_results[:-10]:
            try:
                td_results=result.find_all('td')
                
                stocks_dict['Close'].append(float(td_results[4].text))
                stocks_dict['Stock'].append(td_results[0].text)
                stocks_dict['Symbol'].append(td_results[1].text)
                stocks_dict['Market'].append(market)
                
            except:
                continue
            
            
            
stocks_df=pd.DataFrame(stocks_dict)
stocks_df['Date']=datetime.now().date()
                
                











            
            
