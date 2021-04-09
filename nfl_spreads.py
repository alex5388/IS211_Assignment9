from bs4 import BeautifulSoup
import requests

def main():
  r = requests.get('http://www.footballlocks.com/nfl_point_spreads.shtml').text
  soup = BeautifulSoup(r, 'lxml')

  match = soup.find('span', {'style':'font-size:10.0pt;font-family:verdana'}).find('table')
  print(match.text[143:169])

if __name__=="__main__":
  main()
