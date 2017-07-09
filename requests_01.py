import requests
import json
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.json())

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
print(s.headers)


"""
要获取一个带有状态的 PreparedRequest， 请用 Session.prepare_request() 取代 Request.prepare() 的调用
"""
LoginUrl_GET = 'https://github.com/login'
LoginUrl = 'https://github.com/session'
s = requests.Session()
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
RESULT = s.get(LoginUrl_GET, headers=headers, verify=False)
content = RESULT.content
soup = BeautifulSoup(content, "html.parser")
token = soup.find('input', {'name': 'authenticity_token'})['value']
formData['authenticity_token'] = token
proxies = {
        "http": "http://127.0.0.1:38251",
        "https": "https://127.0.0.1:38251"
    }
req = requests.Request('POST', LoginUrl, data=formData, headers=headers)
prepped = s.prepare_request(req)
resp = s.send(prepped, verify=False, timeout=2, proxies=proxies)
print(resp.status_code)
