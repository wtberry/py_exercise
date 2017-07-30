import csv

fi = open('data/AMEX_daily_prices_N.csv')

fi.readline() # reading the first line of labels for columns
cr = csv.reader(fi)

stock_sum = {}

for line in cr:
    #print(line)
    name, openp, closep = line[1], float(line[3]), float(line[6]) #assigning names for columns
    dif = closep - openp
    stock_sum[name] = stock_sum.get(name, 0) + dif #storing the dif sum by each symbol to dictionary
print('Sum of difference between open and close price for all stock symbol', stock_sum)

print('\nstocks with sum dif less than -40\n')
for k, i in stock_sum.items(): #iterating through the dic for the symbol with price < -40
    if i < -40:
        print(k, i)
fi.close()
