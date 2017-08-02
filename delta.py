import pandas as pd

# import data from data/log_file_1000.csv using pandas DataFrame

data = pd.read_csv('data/log_file_1000.csv', names=['name', 'email', 'fmip', 'toip', 'datetime', 'lat', 'long', 'payload_size'])

matchip_row = data[data.fmip==data.toip].name.count() # compare and index the number of the rows that has the same fmip and toip.

print('The number of rows which have same fmip and toip are', matchip_row)

# number of uniquie values in 'payload' column.

uni = data.payload_size.unique() # numpy.ndarray for some reason

num_unique = len(uni)

print("The number of unique values in 'payload_size' column is", num_unique)

# counting each of unique fmip values 

count_object = data.fmip.value_counts()

print()
print('The highest count:', count_object[0])
print('The lowest count:', count_object[-1])

# printing each column on each line
print()
for column in data.columns:
    print(column)
