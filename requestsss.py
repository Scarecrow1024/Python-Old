import requests
import json
from urllib import request
from bs4 import BeautifulSoup

#help(requests)

try:
    r1 = request.urlopen('https://github.com')
    soup = BeautifulSoup(r1.read().decode(), 'html.parser')
    token = soup.find("input", attrs={"name": "authenticity_token"})['value']
    print(token)
    pp = {'commit': 'Sign in', 'utf8': '✓', 'authenticity_token': '%s' % token, 'login': '819681825@qq.com', 'password': 'zyf941126'}
    r = requests.post('https://github.com/session', data=json.dumps(pp))
    print(r)
except requests.exceptions.ConnectionError as e:
    print(e.strerror)
