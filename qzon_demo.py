# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url = 'https://user.qzone.qq.com/819681825?_t_=0.9925550884716086'
headers = {
        'Host': 'user.qzone.qq.com',  #一般headers里最好不要加host
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
        'Referer': 'Referer: https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone&from=iqq&specifyurl=http%3A%2F%2Fuser.qzone.qq.com%2F819681825',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie': 'eas_sid=v1L4I7a9P7Y2v6W1b4j7170908; pac_uid=1_819681825; tvfe_boss_uuid=3fc746401879b926; mobileUV=1_1591f0dfa9d_9bac1; LW_uid=v1t4O8r6w7l382Y1Q8M6K810r5; same_pc=%7B%7D; pgv_pvi=116076544; RK=PSee8JrbfD; ue_uid=d926877be77270567bb7546a84f539eb; ue_ts=1491646229; ue_uk=52fabc0e0eaf2aad567141f2fd6fe86b; ue_skey=2fd626174795249e0fb9590f67933457; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; LOL_API_W2013_USER_819681825Area=2; LOL_a20170309challenge_bind_819681825=2; LOL_a20170310team_bind_819681825=2; LOL_a20170317comeback_bind_819681825=2; 3g_guest_id=-8896472146952318976; g_ut=2; LW_sid=71S4m9h2T4r9Y4r5n0q9s2j9k2; pgv_info=ssid=s3435256985; pgv_pvid=9923943915; o_cookie=819681825; pgv_si=s8937626624; _qpsvr_localtk=0.986741800202876; qzspeedup=sdch; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; 819681825_todaycount=0; 819681825_totalcount=7031; cpu_performance_v8=5; zzpaneluin=; zzpanelkey=; _qz_referrer=i.qq.com; ptui_loginuin=819681825@qq.com; ptisp=cnc; ptcz=ac92fcfaf7cd1baea85b96b9c46460e8bffa06ffc49cdbf92b55871fd32ff92d; pt2gguin=o0819681825; uin=o0819681825; skey=@sDMt9d4Ir; p_uin=o0819681825; p_skey=TP7vajvixUD19ZyvceBzDEYUEfowxthtKeqIG53fNzo_; pt4_token=suiYX1npKnzpF4FqME5d*D1tZh*IJxwegOjQZTv5mMc_; qzone_check=819681825_1492650582'
        }

web_data = requests.get(url, headers=headers, verify=False)
print(web_data.content.decode())


