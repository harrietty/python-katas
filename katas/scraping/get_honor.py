# Returns the honour for a specific username

import requests
from bs4 import BeautifulSoup

def get_honor(username):
    URL = 'https://www.codewars.com/users/{}'.format(username)
    r = requests.get(URL)
    page = BeautifulSoup(r.text, 'html.parser')
    stats_area = page.find_all(attrs={'class': 'stat-row'})[0]
    honor_section = stats_area.find_all('b')
    return int(honor_section[1].next_sibling.replace(',', ''))