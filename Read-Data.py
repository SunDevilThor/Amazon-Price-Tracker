# Reads Data from Amazon Price Tracker Database

import sqlite3
import pandas as pd

conn = sqlite3.connect('Amazon-Price-Tracker.db')

df = pd.read_sql_query('''SELECT * FROM prices''', conn)
print(df)