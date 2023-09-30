import  os
import json
import requests


url_jianjie = "http://alobgames.com:8080/changedescription"
url_name = "http://alobgames.com:8080/changenickname"



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
    headers = {
    "User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'deflate, gzip',
    'id': str(id),
    "secret":secret,
    'newnickname': name,
    'platform': 'Android',
    'ver': '26',
    'data_ver': '1',
    'X-Unity-Version': '2023.2.0b1'
    }
    return headers

def getdes_ua(id,secret,des):
    headers = {
    	"User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
    	'Accept': '*/*',
    	'Accept-Encoding': 'deflate, gzip',
    	'id': str(id),
    	"secret":secret,
    	'description': des,
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
