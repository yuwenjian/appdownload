# -*- coding: utf-8 -*-
from helper import applist_path,download_report,save_path
import pandas as pd

df = pd.read_csv(save_path)
df.columns = [
    "appName", "apkUrl", "keyword"
]
for url,keyword in zip(df['apkUrl'],df['appName']):
    print(url,keyword)
    download_report(url,keyword)
