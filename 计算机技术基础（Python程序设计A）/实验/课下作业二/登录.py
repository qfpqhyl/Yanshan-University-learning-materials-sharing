login = {
    'kate':'666666',
    'alice':'456',
    'john':'111111'
}
i = 0
while True:
    user = input()
    keyword = input()
    if user in login.keys():
        if login[user] == keyword:
            print("登陆成功")
            break
        else:
            i+=1
            if i ==3:
                print("3次用户名或者密码均有误退出程序")
                break
    else:
        i+=1
        if i ==3:
            print("3次用户名或者密码均有误退出程序")
            break