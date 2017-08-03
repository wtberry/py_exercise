import sqlite3
import pandas as pd

conn = sqlite3.connect('data/log_file.sql') # connecting and opening sql

cur = conn.cursor() # creating cursor
df = pd.read_sql("SELECT name, payload, datetime FROM superheroes WHERE payload > 486000 AND payload < 489500", conn)

print('min payload value:', df.payload.min())
print('max payload value:', df.payload.max())
print('payload median value:', df.payload.median())
print('All payload value:', df.payload)
print('details of df:', df.info())
