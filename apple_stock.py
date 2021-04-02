from bs4 import BeautifulSoup
import requests

r = requests.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL').text
soup = BeautifulSoup(r, 'lxml')

for match in soup.find_all('tr', {'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'}):  #locate historical pricing data in html
    date = match.text[:12]          #parse out date
    price = match.text[30:36]       #parse out closing price
    print(f'{date}    {price}')

