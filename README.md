# Financial_Analysis_Project
Analyzes and build graphs of various bank's stock data from 2006 to 2016

##Description
Uses Python in Jupityer Notebooks for this project. Pulls data from the web (Yahoo) using the library Pandas_Datareader in adjacent to Pandas and Numpy libraries creating a dataframe of the High, Low, Open, Close, Volume, and Adj Close prices for everyday during the time period. 

Initialzes another dataframe that contains the percent change of stock for each day (returns) and builds a pairplot from this dataframe using matplotlib.pyplot. Calculates the standard deviation as well as the day of the highest closing price and day of the lowest closing price for each bank. Moreover, creates histplots with a probability density curve of the returns of City Group and Morgan Stanley.

Next, creates a graph using matplotlib of the closing price throughout the entire ten year period for all banks color coded with a legend. Also, includes a graph of the Closing price and Rolling 30 Day Average of Bank of America for the year 2008

The project now follows with creating and analyzing a correlational heatmap and clustermap. The variable used is the closing price of each bank. Similarly, a clustermap is also made that looks like the heatmap, but has heirarchial relationships depicted as well. 

Finally, using cufflinks and pyplot library, there are dynamic and interactive financial analysis graphs made. First is a candlestick graph of Bank of America for year 2015 which shows the high, low, open, and close prices as well as color coding profit/loss. Second, is a Simple Moving Averages graph of Morgan Stanley for year 2015. Finally, a Bollinger Band Plot of BofA for year 2015. 

