# coding=utf-8
import requests
import http.cookiejar
import ssl
from urllib import parse
from urllib import request

"""
两种方式模拟登录hpu vpn
"""
data = {
    'svpn_name': '311309010130',
    'svpn_password': '*****'
}
def login():
    s = requests.Session()
    s.post('https://vpn.hpu.edu.cn/por/login_psw.csp', data=data, verify=False)
    rr = s.get('https://vpn.hpu.edu.cn/web/1/http/0/218.196.240.97/', verify=False)
    print(rr.text)

def login2():
    # 跳过ssl验证
    ssl._create_default_https_context = ssl._create_unverified_context
    # 保持会话
    cj = http.cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    request.install_opener(opener)
    request.urlopen('https://vpn.hpu.edu.cn/por/login_psw.csp', parse.urlencode(data).encode())
    r = request.urlopen('https://vpn.hpu.edu.cn/web/1/http/0/218.196.240.97/')
    print(r.read())

login()
