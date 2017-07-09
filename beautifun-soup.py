from bs4 import BeautifulSoup
import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
r = requests.get('https://www.douban.com/', verify=False, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
#获取无空格的字符串
for child in soup.ul.stripped_strings:
    print(child)
print(soup.find_all(re.compile("(^<h1)(.*)+(h1>$)")))
print(soup.find_all(['h1','title']))
for child in soup.find_all(attrs={"id":"anony-nav"}):
    for string in child.strings:
        print(str.strip(string))
print(soup.title.find_all(string=True))
#print(soup.select('title').get('href'))
#for tag in soup.find_all(re.compile("^h2")):
#    print(tag.name)

print(soup.select('div > ol > li > a')[0].get('href'))
list1 = soup.find('div', {'list1 movie-charts'})
lis = list1.find_all('li')
"""
for i in lis:
    #for j in i.children:
    #    print(j.string)
    print(i.contents[1].get('href'))
    print(i.contents[1].contents)
print(list1.get('class'))
"""
