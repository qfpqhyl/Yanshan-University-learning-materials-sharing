import random

guess = -1
minNum = 0
maxNum = 100
order = 5  #游戏次数
secret = random.randint(minNum, maxNum)
times = 1

# 定义猜数字函数


def guessnumber():
    global times, minNum, maxNum, guess, order
    for i in range(order):
        guess = int(input("@数字区间{}~{},请输入你猜的数字".format(minNum, maxNum)))
        print("你输入的数字是：", guess)
        if guess == secret:
            print("你猜了{}次，猜对了，真厉害".format(times))
            break
        else:
            print("你猜的数字小于正确答案") if guess < secret else print("你猜的数字大于正确答案")
            if guess < secret:
                # print("你猜的数字小于正确答案")
                minNum = guess
                print("太遗憾了，猜错了，你还有{}次机会".format(order-i-1))
            else:
                # print("你猜的数字大于正确答案")
                maxNum = guess
                print("太遗憾了，猜错了，你还有{}次机会".format(order-i-1))
        if i == order-1 :
            break
        times += 1


print("----------欢迎参加猜数字游戏，请开始----------")
try:
    guessnumber()
except ValueError:
    print("输入内容必须为整数")
    guessnumber()
finally:
    print("游戏结束")