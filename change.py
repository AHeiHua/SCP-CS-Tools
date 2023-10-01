import  os
import json
import requests
from urllib.parse import quote

url_jianjie = "http://alobgames.com:8080/changedescription"
url_name = "http://alobgames.com:8080/changenickname"
url_password = "http://alobgames.com:8080/changepassword"


global user
global password
""" 自动保存密码 """

             
""" 登陆UA """
def getlogin_ua(name,password):
    headers = {
    "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'login': name,
    'password':password,
    'platform': 'Android',
    'ver': '26',
    'data_ver': '1',
    'X-Unity-Version': '2023.2.0b1'
    }
    return headers

""" 更改简介和名字的UA """
def getname_ua(id,secret,name):
    name1 = quote(name)
    headers = {
    "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'id': str(id),
    "secret":secret,
    'newnickname': name1,
    'platform': 'Android',
    'ver': '26',
    'data_ver': '1',
    'X-Unity-Version': '2023.2.0b1'
    }
    return headers
"""更改简介的UA"""
def getdes_ua(id,secret,des):
    des1 = quote(des)
    headers = {
        "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'id': str(id),
        "secret":secret,
        'description': des1,
        'platform': 'Android',
        'ver': '26',
        'data_ver': '1',
        'X-Unity-Version': '2023.2.0b1'
    }
    return headers
""" 更改密码的UA """
def getpassword_ua(id,secret,newpassword):
    headers = {
        "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'id': str(id),
        "secret":secret,
        'newpassword': newpassword,
        'platform': 'Android',
        'ver': '26',
        'data_ver': '1',
        'X-Unity-Version': '2023.2.0b1'
    }
    return headers

def changedes(id,secret,des):
    res = requests.get(url_jianjie,headers=getdes_ua(id,secret,des))
    aaa = res.text
    msg1 = json.loads(aaa)
    if msg1["code"] == "cs_0":
        print("简介更改成功")
    else:
        print("简介更改失败")
    print("更改成功以后 记得重新返回游戏查看效果")
        
def changename(id,secret,name):
    res2 = requests.get(url_name,headers=getname_ua(id,secret,name))
    aa = res2.text
    msg2 = json.loads(aa)
    
    if msg2["code"] == "cs_0":
        print("名称更改成功")
    else:
        print("名称更改失败")
    print("更改成功以后 记得重新返回游戏查看效果")
   
def changepassword(id,secret,password):
    res2 = requests.get(url_password,headers=getpassword_ua(id,secret,password))
    aa = res2.text
    msg2 = json.loads(aa)
    
    if msg2["code"] == "cs_0":
        print("密码更改成功")
    else:
        print("密码更改失败")
    print("更改成功以后 记得重新返回游戏查看效果")
