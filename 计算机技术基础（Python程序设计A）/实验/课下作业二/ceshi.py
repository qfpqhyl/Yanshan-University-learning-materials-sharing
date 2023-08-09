c=0
for i in range(0,3):
    a,b=input(),input()
    if a=="Kate"and b=="666666":
        print("登录成功")
        break
    else:
        c+=1
if int(c)==3:
    print("3次用户名或者密码均有误退出程序")