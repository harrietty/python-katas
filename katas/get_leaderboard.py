'''
This katas gets the list of Codewars Leaderboard scores (aka Honor) in descending order

'''
import os
import requests
from bs4 import BeautifulSoup

def get_leaderboard():
    html_file = os.path.abspath(os.getcwd() + '/data/leaders.html');
    if os.environ['ENV'] == 'TEST':
        if (os.path.exists(html_file)):
            with open(html_file) as f:
                html = f.read()
            f.closed
            need_to_create_file = False
        else:
            html = requests.get('https://www.codewars.com/users/leaderboard').text
            need_to_create_file = True
    
    html = BeautifulSoup(html, 'html.parser');
    if need_to_create_file:
        f = open(html_file, 'w+')
        f.write(html.prettify())
        f.close()

    scores = []
    names = html.find_all(attrs={'data-username': True})
    for name in names:
        score = int(name.find_all('td')[-1].get_text())
        scores.append(score)
    
    return scores
        