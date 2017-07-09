import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

LoginUrl_GET = 'https://github.com/login'
LoginUrl = 'https://github.com/session'
headers = {
        'Host': 'github.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://github.com',
        'Connection': 'keep-alive',
    }
formData = {
        'commit': 'Sign+in',
        'utf8': "✓",
        "login": '819681825@qq.com',
        "password": 'zyf941126',
    }
s = requests.Session()
RESULT = s.get(LoginUrl_GET, headers=headers, verify=False)
content = RESULT.content

soup = BeautifulSoup(content, "html.parser")
token = soup.find('input', {'name': 'authenticity_token'})['value']
formData['authenticity_token'] = token
RESULT = s.post(LoginUrl, data=formData, verify=False)
content = RESULT.content
print(RESULT.url)
print(RESULT.status_code)
print(RESULT.cookies)
print(content.decode())

d = s.get('https://github.com/settings/profile', verify=False)
print(d.text)
