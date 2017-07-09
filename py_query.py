from pyquery import PyQuery as pq
import requests

res = requests.get('https://www.douban.com/')
doc = pq(res.text)
p = doc('#anony-time')
#print(p.attr('id'))
#print(p.attr('id', 'anony-time'))
print(p("a[class='title']"))
print(p("a:eq(0)"))
print(p("img:gt(3)"))
print(p("a:lt(3)"))
print(p(":header"))
print(p("a:contains('豆瓣')"))
print(p("a[class]"))
print(p("a[href='/time']"))
print(p("a img:eq(0)"))