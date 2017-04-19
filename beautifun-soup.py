from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r = requests.get('https://www.douban.com/', verify=False, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.select('div > ol > li > a')[0].get('href'))
list1 = soup.find('div', {'list1 movie-charts'})
lis = list1.find_all('li')
for i in lis:
    #for j in i.children:
    #    print(j.string)
    print(i.contents[1].get('href'))
    print(i.contents[1].contents)
print(list1.get('class'))
