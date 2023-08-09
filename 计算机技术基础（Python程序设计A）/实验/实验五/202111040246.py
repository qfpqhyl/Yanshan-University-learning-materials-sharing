fo = open("学生信息表.csv","a+")

choice = input('''
请选择功能1或2:
1、显示所有学生信息
2、追加新的学生信息
''')

if choice == '1':
    ls = []
    fo.seek(0)
    for line in fo:
        line = line.replace("\n","")
        ls.append(line.split(","))
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            print(ls[i][j],end = "  ")
        print("\n"*0)
elif choice == '2':
    xh = input("请输入学号：")
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    banji = input("请输入班级：")
    ls = [[xh,name,sex,banji]]
    for item in ls:
        fo.write(','.join(item) + '\n')
fo.close()