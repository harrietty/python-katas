'''
Return a 'Leaderboard' object with a position property.

User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer

Positions should be indexed from 1, not 0
'''

from bs4 import BeautifulSoup
import os
import requests
URL = 'https://www.codewars.com/users/leaderboard'

def scrape_top_users():
    saved_data_path = os.path.abspath(os.getcwd() + '/data/leaders.html')

    # If in testing env, get page text from file if it exists
    if os.environ['ENV'] == 'TEST' and os.path.exists(saved_data_path):
        f = open(saved_data_path)
        html = f.read()
        f.close()
    else:
        html = requests.get(URL).text
        if os.environ['ENV'] == 'TEST':
            f = open(saved_data_path, 'w+')
            f.write(html)
            f.close()
    
    def extract_user_obj(section):
        username = section['data-username']
        score = int(section.find_all('td')[-1].get_text())
        clan = section.find_all('td')[-2].get_text().encode('utf-8')
        class User():
            def __init__(self):
                self.name = username
                self.clan = clan.decode('utf-8')
                self.honor = score
        return User()
    
    soup = BeautifulSoup(html, 'html.parser')
    sections = soup.find_all(attrs={'data-username': True})

    class Leaderboard():
        def __init__(self):
            posObj = {}
            for i, item in enumerate(sections):
                posObj[i + 1] = extract_user_obj(item)
            self.position = posObj
    
    return Leaderboard()


    