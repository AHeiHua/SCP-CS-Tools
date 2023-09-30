#! -*- coding:utf-8 -*-
import change
import serverlist
import os
import json
import getservers
import datetime
import requests
global  login_msg
global user
global password
url_login = "http://alobgames.com:8080/login"
global quit
quit = 0
with open("/storage/emulated/0/黑化工具箱/user.txt","a") as f:
    pass
with open("/storage/emulated/0/黑化工具箱/time.txt","a") as f:
    pass
def printmain():
    print("==========================")
    print("<          黑化工具箱          >")
    print("==========================")
time = datetime.datetime.now().ctime()
printmain()
with open("/storage/emulated/0/黑化工具箱/user.txt","r",encoding="utf-8") as f:
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
	with open("time.txt","r") as f:
		last_time = f.read()
else:
	login_msg = "登录失败"

if __name__ == "__main__":
    print(f"当前状态:{login_msg}\n")
    print("上次登录时间:"+time)
    getservers.zhongxin()
    getservers.getversion()
    with open("time.txt","w") as f:
    	f.write(time)
    
    while quit != 1:
        if login_msg == "已登录":
             print(
             "==== 选项 ====\n",
             "1.  更改名称    \n",
             "2.  更改简介    \n",
             "3.  服务器列表  \n",
             "4.  更改账号密码\n",
             "5.  修改游戏密码\n",
             "6.  退出      \n"
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
                with open("user.txt","w",encoding="utf-8") as f:
                    user = input("请输入你的账号:")
                    password = input("请输入你的密码:")
                    f.write(f"{user}\n{password}")
                res1 = requests.get(url_login,headers=change.getlogin_ua(user,password))
             elif num == 5:
                password = input("请输入你要更改的密码:")
                change.changepassword(id=id,secret=secret,password=password)
             elif num == 6:
                quit = 1
             elif num < 6 or num == 0:
                print("错误 请重新选择")
        else:
            with open("user.txt","w",encoding="utf-8") as f:
                user = input("请输入你的账号:")
                password = input("请输入你的密码:")
                f.write(f"{user}\n{password}")
                res1 = requests.get(url_login,headers=change.getlogin_ua(user,password))