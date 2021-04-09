from bs4 import BeautifulSoup
import requests


def main():
    r = requests.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL').text   #get the website
    soup = BeautifulSoup(r, 'lxml')

    print('Date            AAPL Closing Price')
    for match in soup.find_all('tr', {'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'}):  #locate historical pricing data 
        date = match.text[:12]          #parse out date
        price = match.text[30:36]       #parse out closing price

        print(f'{date}    {price}')

if __name__=="__main__":
    main()
