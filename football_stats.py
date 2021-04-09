from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/?sortcol=pts&sortdir=descending').text
soup = BeautifulSoup(source, 'lxml')
list = []

rank = 0

for players in soup.find_all('tr', attrs={'class': 'TableBase-bodyTr'})[:20]:

    rank = rank + 1
    fname = players.text.split()[4]
    lname = players.text.split()[5]
    position = players.text.split()[2]
    team = players.text.split()[3]
    pointsScored = players.text.split()[19]


    print(f"{rank}. {fname} {lname},  {position},  {team},  {pointsScored}")


