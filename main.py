#! -*- coding:utf-8 -*-
import change
import serverlist
import os
import json
import requests
global  login_msg
global user
global password
url_login = "http://alobgames.com:8080/login"
global quit
quit = 0
def printmain():
    print("==========================")
    print("<          黑化工具箱          >")
    print("==========================")

printmain()
with open("user.txt","r",encoding="utf-8") as f:
	    if os.path.getsize("user.txt")==0:
		    user = input("请输入你的账号:")
		    password = input("请输入你的密码:")
		    with open("user.txt","w",encoding="utf-8") as f:
		    	f.write(f"{user}"+ os.linesep + f"{password}")
	    else:
	        user=f.readline().strip()
	        for last_line in f:
	         	password = last_line.strip()
print("帐号:"+user)
print("密码:"+password)
""" 进.行登录操作 """
res1 = requests.get(url_login,headers=change.getlogin_ua(user,password))

aa = res1.text
msg = json.loads(aa)
""" 获取登录密钥 """
if "secret"  in aa:
	secret = msg["secret"]
	id = msg['id']
	login_msg = "已登录"
else:
	login_msg = "登录失败"

if __name__ == "__main__":
    print(f"当前状态:{login_msg}\n")
    while quit != 1:
        if login_msg == "已登录":
             print(
             "==== 选项 ====\n",
             "1.  更改名称    \n",
             "2.  更改简介    \n",
             "3.  服务器列表  \n",
             "4.     退出      \n"
             )
             num = int(input("输入数字选择:"))
             if num == 1:
                name = input("请输入你要更改的名字:")
                change.changename(id=id,secret=secret,name=name)
             elif num == 2:
                des = input("请输入你要更改的简介:")
                change.changedes(id=id,secret=secret,des=des)
             elif num == 3:
             	serverlist.getlist()
             elif num == 4:
                quit = 1
             elif num < 4 or num == 0:
                print("错误 请重新选择")
        else:
            with open("user.txt","w",encoding="utf-8") as f:
             if os.path.getsize("user.txt")==0:
                user = input("请输入你的账号:")
                password = input("请输入你的密码:")
                f.write(f"{user}\n{password}")