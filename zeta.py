import pandas as pd

# reading data from each file
daily = pd.read_csv('data/AMEX_daily_prices_N.csv')
divide = pd.read_csv('data/AMEX_dividends_N.csv')

# printing the first 7 rows of data from each file
print('data of AMEX_daily_prices_N.csv:\n', daily.head(7))
print('data of AMEX_dividends_N.csv:\n', divide.head(7))

# Merge data from each DF into a single DF according to these duidelines 
    # merge on the stock_symbol column, as the key

m1 = pd.merge(daily, divide, on='stock_symbol')
print(m1)
    # merge using the inner join
m2 = pd.merge(daily, divide, how='inner')    
print(m2)

# IDentify any stocks with a Dividend data (Not a Daily price date) of 1991-06-24

jun = m1[m1.date_y=='1991-06-24']
print('1991-jun-24:\n', jun)
# Display to the screen the unique symbol(s) for stocks with that date

print('stock symbols for the date is:', jun.stock_symbol.unique())
