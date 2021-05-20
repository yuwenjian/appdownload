from pandas.io.json import json_normalize
import pandas as pd
import time
import requests
import json
from helper import applist_path,del_used_keyword,save_path

def crawler(page):

    baseUrl = "http://api.scs.mob.com/api/app/search?pageNo=1&pageSize=50&criteriaSearchType=RANGE&techSupportName=" +page;
    headers = {
        "token": "c39ce7c3-90c5-4c03-97b0-95f6abb9794d",
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.190 Safari / 537.36"
    }

    params = (
        ('techSupportName', page),
        ('pageSize', 50),
        ('criteriaSearchType', 'RANGE'),
        ('pageNo', 1)
    )

    response = requests.get(baseUrl, headers=headers, params=params)
    json_data = response.text
    print(json_data)
    # d = json.loads(json_data)
    # result = []
    # for num in range(0, 10):
    #     if d['data']['list'][num]['dayYoy'] <= -20.00 and d['data']['list'][num]['chain'] <= -10.00 and d['data']['list'][num]['weeklyAvgYoy'] <= -10.00:
    #         temp = {
    #             'appName': d['data']['list'][num]['storeName'],
    #             'appkey': d['data']['list'][num]['appKey'],
    #             "businessServiceName": d['data']['list'][num]['businessServiceName']
    #         }
    #         result.append(temp)
    #         print(temp)
    #
    # df = json_normalize(result)
    # df.to_csv(save_path, mode="a+", header=False, encoding='utf-8', index=False)

def KAKBForother(userName):

        baseUrl = "http://api.scs.mob.com/api/app/search?pageNo=1&pageSize=50&criteriaSearchType=RANGE&techSupportName="+ userName
        headers = {
            "token": "c39ce7c3-90c5-4c03-97b0-95f6abb9794d",
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.190 Safari / 537.36"
        }


        response = requests.get(baseUrl, headers=headers)
        json_data = response.text
        print(json_data)
        d = json.loads(json_data)
        result = []
        for num in range(0, len(d['data']['list'])):
            if d['data']['list'][num]['dayYoy'] <= -20.00 and d['data']['list'][num]['chain'] <= -10.00 and d['data']['list'][num]['weeklyAvgYoy'] <= -10.00:
                temp = {
                    'appName': d['data']['list'][num]['storeName'],
                    'appkey': d['data']['list'][num]['appKey'],
                    "techSupportName": d['data']['list'][num]['techSupportName']
                }
                result.append(temp)
                print(temp)

        df = json_normalize(result)
        df.to_csv(save_path, mode="a+", header=False, encoding='utf-8', index=False)

if __name__ == '__main__':

    # for i in range(1, 24):
    #     crawler(i)

    # 技术支持的客户
    userNames=["明世隐","芳芳","蜉蝣","熬兴","风信子","倍墨","狂风","小小凤"]
    for i in range(0, len(userNames)):
        time.sleep(2)
        KAKBForother(userNames[i])
