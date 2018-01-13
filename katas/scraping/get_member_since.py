# Gets the month and year a Codewars member joined

import requests
import re

def get_member_since(username):
    URL = 'https://www.codewars.com/users/{}'.format(username)
    r = requests.get(URL)
    member_since = re.findall(r'Member Since:</b>(\w+\s\d+)', r.text)
    return member_since[0]