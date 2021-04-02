from bs4 import BeautifulSoup
import requests

r = requests.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL').text
soup = BeautifulSoup(r, 'lxml')

for match in soup.find_all('tr', {'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'}):


    date = match.text[:12]
    price = match.text[30:36]
    print(f'{date}    {price}')

