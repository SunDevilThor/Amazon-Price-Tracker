# Amazon Price Tracker
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession
from bs4 import BeautifulSoup
import datetime
import sqlite3

conn = sqlite3.connect('Amazon-Price-Tracker.db')
cursor = conn.cursor()

# Comment out after running once and the table is created. 
cursor.execute('''CREATE TABLE prices(date DATE, asin TEXT, price FLOAT, title TEXT)''')

s = HTMLSession()

asins = ['B099ZCG8T5', 'B08JCRHZGW', 'B09DDJTSPZ']

for asin in asins: 

    url = f'https://www.amazon.com/dp/{asin}'

    r = s.get(url)

    r.html.render(sleep=1)

    price = r.html.xpath('//*[@id="corePrice_feature_div"]/div/span/span[2]')[0].text.replace('$', '').replace(',', '').strip()
    title = r.html.find('#productTitle')[0].text.strip()
    asin = asin 
    date = datetime.datetime.today()

    cursor.execute('''INSERT INTO prices VALUES(?,?,?,?)''', (date, asin, price, title))
    print(f'Added data for {asin}, {price}')
conn.commit()
print('Committed new entries to database')