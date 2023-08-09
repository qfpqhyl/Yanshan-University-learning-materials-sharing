import random
# 定义手势类型
allList = ['石头','剪刀','布']
# 定义获胜的情况
winList = (['石头','剪刀'],['剪刀','布'],['布','石头'])
# 用户输入
chnum = -1
prompt = '''
===欢迎参加石头剪刀布游戏===

请选择：
0   石头
1   剪刀
2   布
3   我不想玩了

==========================
请选择相应的数字：'''

while True:
    chnum = input(prompt)
    if chnum not in ['0','1','2','3']:
        print("无效的选择,请选择0/1/2/3")
        continue
    if chnum == '3':
        break
    cchoice = allList[eval(chnum)]
    uchoice = allList[random.randint(0,2)]
    print("您选择了：{}\n计算机选择了{}".format(cchoice,uchoice))
    if cchoice == uchoice:
        print("平局")
    elif [cchoice,uchoice] in winList:
        print("你赢了！！！")
    else:
        print("你输了...")