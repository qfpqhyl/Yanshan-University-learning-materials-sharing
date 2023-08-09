def Rect():  #绘制600*400矩形
    t.color("red","red")
    t.penup()
    t.goto(-300,200)
    t.pendown()
    t.begin_fill()
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.end_fill()
def Star(x,y,m,n):  #x,y 为五角星的起笔点，m为姿态角度，n为大小
    t.penup()
    t.color("yellow","yellow") #设置画笔色和填充色
    t.goto(x,y)  #补全一行移动到起笔点代码
    t.seth(m)    #补全一行设置姿态角度代码
    t.pendown()
    t.begin_fill()   
    for i in range(5):
        t.forward(n)                 #请补五角星5个笔画绘制代码
        t.right(144)
    t.end_fill()
    
import turtle as t
t.setup(1200,800,100,100) #设置画布
t.speed(0)
t.pensize(5)
t.hideturtle()
Rect()              #调用绘制矩形红布函数
Star(-250,100,0,120)  #分别调用五角星绘制函数
Star(-100,150,60,30)
Star(-50,100,30,30)
Star(-50,50,0,30)
Star(-100,0,-30,30)
t.done()