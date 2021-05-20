# -*- coding: utf-8 -*-
import os
import requests

DATA_FOLDER = 'Data'
applist_path = 'applist.txt'
save_path = 'apps.csv'

def del_used_keyword(keyword):
    print(keyword)
    lines = [l for l in open(applist_path, "r",encoding='utf-8') if l!=keyword]
    print(lines)
    fd = open(applist_path, "w",encoding='utf-8')
    fd.writelines(lines)
    fd.close()

def download_report(url, filename):
    res = requests.get(url)
    fp = open(os.path.join(DATA_FOLDER, filename+'.apk'), "wb")
    fp.write(res.content)
    fp.close()