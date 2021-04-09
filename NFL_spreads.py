from bs4 import BeautifulSoup
import requests

def main():
    r = requests.get('http://www.footballlocks.com/nfl_point_spreads.shtml').text   #website to scrape
    soup = BeautifulSoup(r, 'lxml')

    match = soup.find('span', {'style':'font-size:10.0pt;font-family:verdana'}).find('table')  #find the data location

    Favorite = match.text[143:153]
    Spread = match.text[154:156]
    Underdog = match.text[159:167]
    print('Favorite      Spread      Underdog')   #Headers
    print(f'{Favorite}     {Spread}         {Underdog}')  #Teams and Spread

if __name__=="__main__":
    main()