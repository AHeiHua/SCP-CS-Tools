import os
import json
url_jianjie = "http://alobgames.com:8080/changedescription"
url_name = "http://alobgames.com:8080/changenickname"
url1 = "http://alobgames.com:8080/login"
print("更改成功以后 记得重新返回游戏查看效果")
ch = True
global user
global password
with open("user.txt","r",encoding="utf-8") as f:
	    if os.path.getsize("user.txt")==0:
		    user = input("请输入你的账号:")
		    password = input("请输入你的密码:")
		    with open("user.txt","a",encoding="utf-8") as f:
		    	f.write(f"{user}\n{password}")
	    else:
	        user=f.readline()
	        for last_line in f:
	         	password = last_line
	         
name = input("请输入你要更改的名字:")
change = input("是否要更改简介(1.ok 2.no):")

jianjie = False
if change ==  "1":
	jianjie = True
headers1 = {
"User-Agent": 'UnityPlayer/2023.2.0b1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)',
'Accept': '*/*',
'Accept-Encoding': 'deflate, gzip',
'login': user,
'password':password,
'platform': 'Android',
'ver': '26',
'data_ver': '1',
'X-Unity-Version': '2023.2.0b1'
}
res1 = requests.get(url1,headers=headers1)

aa = res1.text
msg = json.loads(aa)
secret = msg["secret"]
id = msg['id']
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
res = requests.get(url_name,headers=headers)
aaa = res.text
msg1 = json.loads(aaa)
if jianjie:
	des = input("请输入你要更改的简介")
	headers2 = {
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
	res2 = requests.get(url_jianjie,headers=headers2)
	aa = res2.text
	msg2 = json.loads(aa)
	if msg2["code"] == "cs_0":
		print("简介更改成功")
	else:
		print("简介更改失败")
	
	
if msg1["code"] == "cs_0":
	print("改名成功")
else:
	print("改名失败")
