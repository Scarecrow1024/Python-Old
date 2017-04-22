# -*- coding:utf-8 -*-
__author__ = 'ZYF'
__data__ = '2017.04.19'

import requests
import json
import time
import xlwt
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning

"""
不显示SSL警报
"""
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Spider(object):
    def __init__(self):
        self.keyword = input('请输入职位：').strip()

    """
    获取数据
    """
    def getData(self, url):
        user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \(KHTML, like Gecko) Element Browser 5.0',
                       'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                       'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
                       'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \Version/6.0 Mobile/10A5355d Safari/8536.25',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \Chrome/28.0.1468.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                       'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000 Chrome/39.0.2146.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.277.400 QQBrowser/9.4.7658.400',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 TheWorld 7',
                       'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
        index = random.randint(0, 20)
        user_agent = user_agents[index]
        # url = 'https://www.lagou.com/jobs/positionAjax.json?first=true&pn=%d&kd=%s&city=杭州' % (pages, self.keyword)
        headers = {
                'User_agent': user_agent,
                'cookie': 'user_trace_token=20161231133515-8cce936e9adc4b43abe2959e6d2f26ed; LGUID=20161231133515-e8366cd1-cf1a-11e6-b892-525400f775ce; isCloseNotice=0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=15; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; TG-TRACK-CODE=index_user; login=false; unick=""; _putrc=""; JSESSIONID=B627AC3354F9AC597B81F85FC552EA13; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1492700323,1492828798,1492840842,1492841253; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1492842822; _ga=GA1.2.80659696.1483162516; LGSID=20170422140041-03fdd1ec-2721-11e7-93f6-525400f775ce; LGRID=20170422143340-9ffaa58c-2725-11e7-ae1d-5254005c3644'
            }
        proxies = {"http": "http://115.159.41.73:80"}
        data = requests.get(url, verify=False, headers=headers, proxies=proxies)
        return data.text

    # 返回一个小列表存一页的数据
    def getPosition(self, url):
        res = self.getData(url)
        try:
            data = json.loads(res)
            result = data['content']['positionResult']['result']
            l_list = []
            if result is not None:
                for i in result:
                    main = []
                    main.append(i['companyFullName'])
                    main.append(i['financeStage'])
                    main.append(i['positionName'])
                    main.append(i['positionLables'])
                    main.append(i['salary'])
                    main.append(i['city'])
                    main.append(i['education'])
                    main.append(i['workYear'])
                    main.append(i['jobNature'])
                    main.append(i['createTime'])
                    l_list.append(main)
            else:
                l_list.append([])
            return l_list
        except json.decoder.JSONDecodeError as e:
            print(e)
    def saveAll(self):
        book = xlwt.Workbook()
        sheet = book.add_sheet(str(self.keyword), cell_overwrite_ok=True)
        container = self.getAll()
        print('准备将数据存入表格...')
        heads = [u'公司全名', u'融资状况', u'工作名称', u'标签', u'薪酬', u'城市', u'学历要求', u'经验要求', u'工作类型', u'数据创建时间']
        ii = 0
        for head in heads:
            sheet.write(0, ii, head)
            ii += 1
        i = 1
        for list in container:
            j = 0
            for one in list:
                sheet.write(i, j, str(one))
                j += 1
            i += 1
        book.save(str(self.keyword) + '.xls')
        print('录入成功！')

    # 获取全部页数
    def getAll(self):
        pn = input('输入要爬取得页数：')
        container = []
        for page in range(1, int(pn)+1):
            self.url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&first=true&pn=' + str(page) + '&kd=' + str(
                    self.keyword)
            po_list = self.getPosition(self.url)
            time.sleep(3)
            print('第', page, u'页完毕')
            #print(po_list)
            try:
                container = container + po_list
            except TypeError as e:
                print(e)
                container = container
        return container


if __name__ == "__main__":
    spider = Spider()
    spider.saveAll()
