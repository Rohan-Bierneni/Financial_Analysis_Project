# Financial_Analysis_Project
Analyzes and build graphs of various bank's stock data from 2006 to 2016

## Description
Uses Python in Jupityer Notebooks for this project. Pulls data from the web (Yahoo) using the library Pandas_Datareader in adjacent to Pandas and Numpy libraries creating a dataframe of the High, Low, Open, Close, Volume, and Adj Close prices for everyday during the time period. 

Initialzes another dataframe that contains the percent change of stock for each day (returns) and builds a pairplot from this dataframe using matplotlib.pyplot. Calculates the standard deviation as well as the day of the highest closing price and day of the lowest closing price for each bank. Moreover, creates histplots with a probability density curve of the returns of City Group and Morgan Stanley.

Next, creates a graph using matplotlib of the closing price throughout the entire ten year period for all banks color coded with a legend. Also, includes a graph of the Closing price and Rolling 30 Day Average of Bank of America for the year 2008

The project now follows with creating and analyzing a correlational heatmap and clustermap. The variable used is the closing price of each bank. Similarly, a clustermap is also made that looks like the heatmap, but has heirarchial relationships depicted as well. 

Finally, using cufflinks and pyplot library, there are dynamic and interactive financial analysis graphs made. First is a candlestick graph of Bank of America for year 2015 which shows the high, low, open, and close prices as well as color coding profit/loss. Second, is a Simple Moving Averages graph of Morgan Stanley for year 2015. Finally, a Bollinger Band Plot of BofA for year 2015. 

## Installation
This project requires pandas, numpy, matplotlib, pandas-datareader, seaborn, plotly, and cufflinks libraries. To install these on your computer, in your terminal or command prompt, type pip install following by the name of the library

For example, to install pandas_datareader, type:
`pip install pandas_datareader`

For more information on these libraries the links:
- https://github.com/pandas-dev/pandas
- https://github.com/numpy/numpy
- https://github.com/matplotlib/matplotlib
- https://github.com/pydata/pandas-datareader 
- https://github.com/seaborn/seaborn
- https://github.com/plotly/plotly.py
- https://github.com/santosjorge/cufflinks

## Visuals
<img width="1000" alt="Screen Shot 2022-03-31 at 12 06 59 AM" src="https://user-images.githubusercontent.com/102715043/160997472-c786416d-25aa-4999-9f34-31a968f82404.png">
<img width="729" alt="Screen Shot 2022-03-31 at 12 07 53 AM" src="https://user-images.githubusercontent.com/102715043/160997584-64e19890-e578-46da-84e5-c4e212ad80d3.png">
<img width="452" alt="Screen Shot 2022-03-31 at 12 08 10 AM" src="https://user-images.githubusercontent.com/102715043/160997625-7405fd70-7821-4087-8932-22155c07f25f.png">
<img width="1096" alt="Screen Shot 2022-03-31 at 12 08 26 AM" src="https://user-images.githubusercontent.com/102715043/160997674-9141db69-095f-4bc1-8dba-3d7d2cae301d.png">


