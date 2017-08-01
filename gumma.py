import csv

fi = open('data/AMEX_daily_prices_N.csv', 'r')

fi.readline() # reading the first line(labels)

cr = csv.reader(fi)

names = set() # creating an empty set to store the stock symbols 

for line in cr:
    stock, openp, closep = line[1], float(line[3]), float(line[6])
    if openp in range(31, 420) and closep in range(33, 422):
        names.add(stock)

fi.close()

fw = open('gumma_out.csv', 'w')
sname = list(names) # converting set to list
stock_str = ','.join(e for e in sname) # converting list to one string
print(stock_str)
fw.write(stock_str)
fw.close()
