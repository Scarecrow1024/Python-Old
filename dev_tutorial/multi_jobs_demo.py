# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 18:11:55 2014

@author: chongdata.com
"""

import datetime
import os
import requests


def post_requst(end_point, params, files):
    # files={'report.xls': open('report.xls', 'rb')
    r = requests.post(end_point,
                      files={'report.xls': open('report.xls', 'rb')})

# 获得email帐号(username)和密码(password) ,需要到这里注册 http://chongdata.com/old/register.php
username = "819681825@qq.com"
password = "zyf941024"
root = 'https://www.chongdata.com/ocr/dev_api_v2'
end_point_submit_job = root + '/submit_job.php'
end_point_job_status = root + '/job_status.php'
end_point_get_res = root + '/get_res.php'

files_to_reco = ['./sample1.png',
                 './sample2.png',
                 './sample3.png',
                 './sample4.png',
                 './sample5.png',
                 './sample6.png',
                 './sample7.png',
                 './sample8.png',
                 './sample9.png',
                 './sample10.png',
                 './sample11.png']

cur_dir = os.path.dirname(os.path.realpath(__file__))
from_time = datetime.datetime.now()
job_ids = []

if __name__ == "__main__":
    for file_to_reco in files_to_reco:
        abs_path_file_to_reco = os.path.join(cur_dir, file_to_reco)

