# Boston Consulting Group (BCG) Top 10 most Innovative Companies of 2023
Boston Consulting Group released it's list of the 50 most innovative companies for the year 2023. For this project, I used the list to pick the top 10 companies and performed a stock analysis so see if innovation for each of the companies was reflective of it's stock performance.

## Getting started
To get the stock data for a company, simply run `get_data.py AAPL.csv` in the command line or terminal. This will download Apple stock data. To get the data for another company, say Amazon, replace the Apple ticker symbol (AAPL) with Amazon's (AMZN). Don't forget to add `.csv` because we want the data collected as a csv file.

## Preparing data for analysis
Run the jupyter notebook file `clean_data.ipynb` to clean the data and perform calculations to create new columns such as moving averages.

The cleaned dataset for each company is then exported as a csv file, overwriting the earlier version.

## Analyze data
Tableau was used to analyze the data and to create an interactive dashboard that makes visualizing the analysis easier.