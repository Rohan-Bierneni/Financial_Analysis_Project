#!/usr/bin/env python
# coding: utf-8

# In[33]:


#Import libraries
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime as dt

import seaborn as sns
sns.set_style('whitegrid')

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#For dynamic graphs
import plotly as pt
import cufflinks as cf
cf.go_offline()

#Sets the renderer globally to "svg"
#Makes the plotly grpahs static so can view in GitHub
#Delete these bottom two lines in order to make plotly graphs interactive and dynamic
#import plotly.io as pio
#pio.renderers.default = "svg"


# In[2]:


#Initialize objects for the period in which data will be collected
start = dt.datetime(2006, 1, 1)
end = dt.datetime(2016,1,1)


# In[4]:


#Use data_reader to load data from yahoo into a Dataframe
BAC = data.DataReader("BAC", 'yahoo', start, end)
C = data.DataReader("C", 'yahoo', start, end)
GS = data.DataReader("GS", 'yahoo', start, end)
JPM = data.DataReader("JPM", 'yahoo', start, end)
MS = data.DataReader("MS", 'yahoo', start, end)
WFC = data.DataReader("WFC", 'yahoo', start, end)


# In[5]:


#Test if data loaded properly
C.head()


# In[6]:


#List to be used as level 1 in the heirachcial index
#Level 2 will be the Stock Info (High, Low, Open, Close, etc...)
tickers = ["BAC", "C", "GS", "JPM", "MS", "WFC"]


# In[7]:


#Join the various dataframes into a single heirarchial index dataframe
bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC], keys=tickers, axis=1)


# In[8]:


bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# In[9]:


#Verify that data is formatted correctly
bank_stocks.head()


# In[10]:


#Returns the lowest Closing value for each respective bank throughout the entire dataset
bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()


# In[11]:


#Create a new dataframe for returns
#Return for a particular stock is the (close price - open price)/(open price)
#Can also be said as the percent change of the stock from trading during the respective day
returns = pd.DataFrame()


# In[12]:


for x in tickers:
    returns[x + " Returns"] = bank_stocks[x]["Close"].pct_change()


# In[13]:


returns.head()


# In[14]:


#Creates a pairplot of the returns dataframe
#The diagonal showes histograms depicting the distribution of single variables (returns for each respective bank)
#The upper half and lower half show the correlation between two variables (returns of one bank compared to another)
sns.pairplot(returns[1:])


# In[15]:


#Returns the dates on which the respective bank had lowest percent change in trading that day
#Note that 4 banks had lowest returns in early 2009 depicting the stock market crisis
returns.idxmin()


# In[16]:


#Returns the dates on which the respective bank had the highest percent change in trading that day
returns.idxmax()


# In[17]:


#Shows the standard deviation of trading throughout entire period
returns.std()


# In[18]:


#Standard deviation for only the year 2015
returns.loc['2015-01-01':'2015-12-31'].std()


# In[32]:


#Creates a histogram of Returns vs. Number of Occurences for Morgan Stanley 
#Also includes a probability density curve of the histogram
sns.displot(x=returns.loc['2008-01-01':'2008-12-31']["MS Returns"], kde=True, bins=80)


# In[20]:


#Another histogram with a probability density curve for City Group 
sns.displot(x=returns.loc['2008-01-01':'2008-12-31']["C Returns"], kde=True, bins=80)


# In[21]:


#Create a dataframe of closing prices each day for respective banks
#Note that resulting dataframe is not heirarchial
#Use this to make a plot of stock prices throughout entire timeline
bank_stocks.xs(key='Close',axis=1,level='Stock Info')


# In[22]:


#Use matplotlib to plot all stocks on a single graph to compare
#Note the major drop in City Group and other stocks during stock market crisis of 2008
plt.figure(figsize=(12, 5))
plt.plot(bank_stocks.xs(key='Close',axis=1,level='Stock Info'))
plt.legend(tickers)


# In[23]:


#Create a graph of the 30 day Rolling Moving Average vs. Closing Price of Bank of America stock
plt.figure(figsize=(12, 5))
plt.plot(bank_stocks.loc['2008-01-01':'2008-12-31']["BAC"]["Close"], label="BAC Close")
plt.plot(bank_stocks.loc['2008-01-01':'2008-12-31']["BAC"]["Close"].rolling(30).mean(), label="30 Day AVG")
plt.legend()


# In[24]:


#Create a correlation heatmap using seaborn
#Data will be the closing price of each respective bank
corr = bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr()


# In[25]:


corr.head()


# In[26]:


sns.heatmap(corr, annot=True, cmap="Reds")


# In[27]:


#Creating a clustermap using seaborn library
#The clustermap rearranges the rows and colums so that similar data appears next to each other
#For example, in upper half of diagonal, lower correlation are grouped together (0.68,0.25,0.13)
#while higher correlation are grouped together (0.94,0.93)
sns.clustermap(corr, annot=True, cmap="Reds")


# In[34]:


#Uses cufflinks and plotly to create an interactive graph
#This graph is a candlestick graph that shows High, Low, Open, and Close of Bank of America for entire time period
bank_stocks.loc['2015-01-01':'2016-01-01']["BAC"].iplot(kind="candle")


# In[29]:


MS['Close'].loc['2015-01-01':'2016-01-01']


# In[30]:


#This is a graph of the Simple Moving Averages for Morgan Stanley Closing Prices
#The SMA's taken are for 13 days, 21 days, and 55 days
#Note that the intersection or inflection points for the SMA's results in the direction of the trend to flip
#For example, intersection point in Sep 2015 caused the flip from growing to falling
bank_stocks.loc['2015-01-01':'2015-12-31']["MS"]["Close"].ta_plot(study='sma', 
    periods=[13,21,55], title='Simple Moving Averages')


# In[31]:


#Creates a Bollinger Band Plot of Bank of America for the year 2015
bank_stocks.loc['2015-01-01':'2015-12-31']["BAC"]["Close"].ta_plot(study='boll', 
    periods=14, title='Bollinger Band Plot')


# In[ ]:




