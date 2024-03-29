from urllib import request
from urllib import parse
import http.cookiejar

import urllib

data = parse.urlencode({'name': 'xiaoming'})
print(data)
try:
    #install cookie
    cj = http.cookiejar.CookieJar()
    opener = request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    request.install_opener(opener)
    #install http_proxy
    proxy_support = request.ProxyHandler({'sock5': 'localhost:1080'})
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)
    response = request.urlopen('https://www.github.com')
    #help(response)
    print(response.getheaders())
    print(response.getcode())
    #help(request)
except urllib.error.HTTPError as e:
    print(e.code)
except urllib.error.URLError as e:
    print(e.strerror)
    print(e.reason)
except Exception as e:
    print(e)
