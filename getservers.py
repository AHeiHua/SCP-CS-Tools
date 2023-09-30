import os
import requests
import json

def zhongxin():
    url = "http://alobgames.com:8080/getstatus"
    res = requests.get(url)
    if res.status_code == 200:
        print("中心服务器正常")
    else:
        print("中心服务器没了")
        
def getversion():
    url = "http://alobgames.com:8080/getversion"
    headers = {
    "User-Agent": "UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)",
    "Accept": "*/*",
    "Accept-Encoding": "deflate, gzip",
    "type": "1",
    "X-Unity-Version": "2023.2.0b1"
    }
    res = requests.get(url,headers=headers)
    version = res.text
    print("当前是第"+version+"个版本")