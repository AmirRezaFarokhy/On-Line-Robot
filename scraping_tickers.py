import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

url = "http://www.tsetmc.com/loader.aspx?ParTree=111C1115"
req = requests.get(url)
df = pd.read_html(req.text)

lst = [l[0][1:] for l in df[-1:]]

tickers = []
for t in lst[0]:
	tickers.append(t.split(",")[1])

with open("ticker.txt", "w", encoding='utf-8') as file:
	file.write(str(tickers))
	file.close()

#print(tickers)
