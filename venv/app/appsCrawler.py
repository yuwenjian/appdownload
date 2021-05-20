# -*- coding: utf-8 -*-
from pandas.io.json import json_normalize
import pandas as pd
import time
import requests
from helper import applist_path,del_used_keyword,save_path

def crawler(keyword):
    headers = {
        'authority': 'android.myapp.com',
        'content-length': '0',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://android.myapp.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://android.myapp.com/myapp/search.htm?kw=^%^E5^%^BE^%^AE^%^E4^%^BF^%^A1',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'session_uuid=2ef3e91b-da69-4b31-8266-84533187f797; JSESSIONID=aaaPlwVqLJC5KbIfPPzCx; pgv_info=ssid=s4521913380; ts_refer=www.google.com/; pgv_pvid=9149416266; ts_uid=7318114680; ts_last=android.myapp.com/myapp/search.htm',
    }

    params = (
        ('kw', keyword),
        ('pns', '^'),
        ('sid', ''),
    )

    response = requests.post('https://android.myapp.com/myapp/searchAjax.htm', headers=headers, params=params)
    result = []
    # for i in response.json()['obj']['appDetails']:
    temp = {
        'appName': response.json()['obj']['appDetails'][0]['appName'],
        'apkUrl': response.json()['obj']['appDetails'][0]['apkUrl'],
        'versionName': response.json()['obj']['appDetails'][0]['versionName'],
        'keyword': keyword
    }
    print(temp)
    result.append(temp)
    df = json_normalize(result)
    df.to_csv(save_path, mode="a+", header=False, encoding='utf-8', index=False)

if __name__ == '__main__':
    with open(applist_path,'r',encoding='utf-8') as f:
        keywords = f.readlines()
        keywords = [keyword.strip() for keyword in keywords]
    for keyword in keywords:
        print(keyword)
        time.sleep(2)
        crawler(keyword)
        del_used_keyword(keyword+'\n')