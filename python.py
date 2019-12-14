print("hellow world")

print(100+200)

print("adsdas", "asdasdasd", 100)

a = 100
if a >= 12:
	print (a)
else:
	print(-a)

print('\'\"\\')

print('s\tsasda\nsadjakdalk\tjaskldjsa')

print(r'//////\\\w\qe\q\qwe\qw\e')

print('''line
line2
line3''')


a = 123
print(a)
a = 'dasdas'
print(a)

print('''Hello,
Lisa!''')

age = 18
if age >= 18:
	print('adult')
elif age >= 50:
	print('the old')
else:
	print ('children')



birth = 3

if birth < 2000:
    print('00前')
else:55


names = ['s','ss','sss']
for name in names:
 	print(name)


sum = 0
for x in range(100):
	sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print (name)



n = 1555
while n <= 100:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)
print ('end')

def name():
	name = input('please enter your name')
	print ('hi, ' + name + '!')

def calc():
	temp = int(input('please enter the number between 1 and 100'))
	if 1 <= temp <= 100:
		print('good job')
	else:
		print('try again')

a = r'C:\Program Files\FishC\Good\\'
print(a)


def game():
	import random
	guess = random.randint(1,10)
	temp = input('please enter a number between 1 and 10\n')
	num = int(temp)
	i = 0
	while i < 2:
		if num == guess:
			print('bingo')
			print('congradulation')
			break
		if num > guess:
			print('bigger')
		if num < guess:
			print('smaller')
		temp = input('try again\n')
		num = int(temp)
		i += 1
		if i > 1:
			print('no chance')
	print('gg')


def game():
	import random
	times = 3
	secret = random.randint(1,10)
	print('------------------我爱鱼C工作室------------------')
	guess = 0
	print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
	while (guess != secret) and (times > 0):
	    temp = input()
	    while not temp.isdigit():
	        temp = input("抱歉，您的输入有误，请输入一个整数：")
	    guess = int(temp)
	    times = times - 1 # 用户每输入一次，可用机会就-1
	    if guess == secret:
	        print("我草，你是小甲鱼心里的蛔虫吗？！")
	        print("哼，猜中了也没有奖励！")
	    else:
	        if guess > secret:
	            print("哥，大了大了~~~")
	        else:
	            print("嘿，小了，小了~~~")
	        if times > 0:
	            print("再试一次吧：", end=" ")
	        else:
	            print("机会用光咯T_T")
	print("游戏结束，不玩啦^_^")

def test():
	temp = input('please enter a number\n')
	num = int(temp)
	i = 1
	while num > 0:
		print(i)
		i += 1
		num -= 1 

def test():
	temp = input('请输入一个整数:')
	number = int(temp)
	while number:
	    i = number - 1
	    while i:
	        print(' ', end = '')
	        i = i - 1
	    j = number
	    while j:
	        print('*', end = '')
	        j = j - 1
	    print()
	    number = number - 1





def test():
	temp = input('please enter a number\n')
	num = int(temp)
	while num > 0 :
		j = num
		i = num - 1
		while i > 0:
			print(' ', end = '')
			i -= 1
		while j > 0:
			print('*', end = '')
			j -= 1
		print()
		num -= 1

def test():
	temp = input('请输入一个整数:')
	number = int(temp)
	while number:
	    i = number - 1
	    while i:
	        print(' ', end = '')
	        i = i - 1
	    j = number
	    while j:
	        print('*', end = '')
	        j = j - 1
	    print()
	    number = number - 1



def test():
	num = 10
	i = num
	while num > 0:
		print(i)
		num -= 1




def test():
	temp = input('please enter the year\n')
	while not temp.isdigit():
		temp = input('please enter a number\n')
	year = int(temp)
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and year % 100 != 0:
		print(temp + ' is run year')
	else:
		print(temp + ' is not run year')

def odd():
	for i in range(1,101:
		if i % 2 != 0:
			print(i)

def test():
	for i in range(1,1000):
		if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
			print(i)
			

def test():
	for i in range(100,1000):
		string = str(i)
		total = 0
		for j in string:
			num = int(j)
			total += num ^ 3
		if i == total:
			print(i)
		else:
			print('nothing')	

def part():
	total = 0
	for j in '123':
		num = int(j)
		total += num ** 3
	print(total)

def code():
	password = 'mwj960507'
	times = 3
	temp = input('please enter the password\n')
	txt = 'times only'
	while times > 0:
		if temp == password:
			print('welcome to back')
			break 
		elif '*' in temp:
			print('%d %s' % (times,txt))
			temp = input('please try again\n')
			continue
		else:
			times -= 1
			print('%d %s' % (times,txt))
			temp = input('please try again\n')
			
def test():			
	list1 = []
	for x in range(10):
	    for y in range(10):
	        if x%2 == 0:
	            if y%2 != 0:
	                list1.append((x, y))


list1 = []
for x ,y in range(10):
	if x%2 == 0 and y%2 != 0:
		list1.append((x, y))

 a = 'a\
 asdadadsa'

 a = '''asdsadasd
 sdasdadad'''

def check():
	symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	nums = '0123456789'
	password = input('please enter the password\n')
	pass_len = len(password)

	while password.isspace() or pass_len == 0:
		password = input('your password is null or include space, please try again\n')

	if pass_len >= 16:
		len_flag = 3
	elif pass_len > 8:
		len_flag = 2
	else:
		len_flag = 1

	str_flag = 0
	for each in password:
		if each in symbols:
			str_flag += 1
			break

	for each in password:
		if each in chars:
			str_flag += 1
			break	

	for each in password:
		if each in nums:
			str_flag += 1
			break

	if len_flag == 1 or str_flag == 1:
		print('low')
	elif len_flag == 2 or str_flag == 2:
		print('medium')
	else:
		print('high')

def min(x):
    least = x[0]

    for each in x:
        if each < least
            least = each
    return least


def sum(*x):
    result = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else: 
            continue
    return result

def powder(x, y):
    num = 1
    while y > 0:
        num *= x
        y -= 1
    return num

def test(*x, base = 3):
    sum = 0
    for i in x:
        sum += i
    if x[-1] != 5:
        result = sum * 3
    else:
        result = (sum - 5) * 5
    return result

def test(ostr, sub):
    len1 = len(ostr)
    count = 0
    if sub not in ostr:
        print('not found')
    else:
        for each in range(len1 - 1):
            if ostr[each] == sub[0]:
                if ostr[each + 1] == sub[1]:
                    count += 1
        print ('%dtimes' % count)

def a():
    print('aaaaaaaa')
    b()
def b():
    print('bbbbbbbb')

def test():
    sent = input('please enter a sentence\n')
    len_s = len(sent)
    flag = 0
    for i in range(len_s - 1):
        if sent[i] != sent[-i -1]:
            flag += 1
    if flag == 0:
        print('interesting sentence')
    else:
        print('nononononono')

def funX(x):
    def funY(y):
        return x * y
    return funY(y)

a = 'hi'
def fun1():
    global a
    a = 'baby'
    return fun2(a)
def fun2(a):
    a += '520'
    fun3(a)
    return a
def fun3(a):
    a = 'marcus'
    print(a)  

def count(*x):
    length = len(x)
    for i in range(length):
        char = 0
        num = 0
        space = 0
        other = 0
        for each in x[i]:
            if each.isalpha():
                char += 1
            elif each.isdigit():
                num += 1
            elif each == ' ':
                space += 1
            else:
                other += 1
        print('N0.%d string has char:%d, num:%d, space:%d, other:%d' % (i+1, char, num, space, other))


def test():
    str1 = input('please enter a sentence\n')
    list = []
    for each in str1:
        if each not in list:
            print(each, str1.count(each))
            list.append(each)

def test(x):
    if x % 2:
        return x
    else: 
        print('aaaaa')

def ten22():
    num = int(input('please enter a number\n'))
    list = []
    while num > 0:
        yu = num % 2
        num = num // 2
        list.append(yu)
    for each in list:
        print(each, end = '')

def test():
    str1 = input('please enter a sentence: ')
    str2 = input('2222222222222: ')
    print(str1)
    print(str2)





def comm():
    d = {'marcus': 13122370062}
    print('.........欢迎来到通讯录..........')
    print('.........1. 查询联系人..........')
    print('.........2. 插入联系人..........')
    print('.........3. 删除联系人..........')
    print('.........4. 退出通讯录..........')
    code = int(input('请输入指令代码： '))
    while code != 4:
        if code == 1:
            name = input('请输入姓名： ')
            if name in d:
                print(name, ': ',d[name])
            else:
                print('查无此人，请重试')
        elif code == 2:
            name = input('请输入姓名： ')
            if name in d:
                print('已有此人——>%s : %s' & (name, d[name]))
                temp = input('是否修改（YES/NO)')
                if temp == 'YES' or 'yes':
                    phone = input('请输入电话： ')
                    d[name] = phone
                    print('修改成功')
                else:
                    continue
            else:
                phone = input('请输入电话： ')
                d[name] = phone
                print('添加成功')
        elif code == 3:
            name = input('请输入姓名： ')
            if name in d:
                del d[name]
                print('删除成功！')
            else:
                print('查无此人，请重试')
        code = int(input('请输入指令代码： '))
    print('感谢使用本程序')

def test():
    a = 'yes'
    if a == 'YES' or 'yes':
        print(1)
    else:
        print(2)
d = {'marcus': 13122370062}
name = 'marcus'
print('已有此人——> %s: %s' % (name, d[name])
print('已有此人——> %s: %s' % ('12312312', 'asdadas')

def fw(file_name):
    f = open(file_name, 'w')
    input1 = input('please enter some words, w: means end\n')
    if input1 != 'w:':
        f.write(input1)
    f.close()
def test():
    file_name = input('please enter the file name\n')
    fw(filem_name)

def compare(file_name1, file_name2):
    f1 = open(file_name1, 'r')
    f2 = open(file_name2, 'r')
    count = 0
    diff = []
    for each in f1:
        count += 1
        each2 = f2.readline()
        if each != each2:
            diff.append(count)
    if len(diff) == 0:
        print('same')
    else:
        print('there are %d differences: \n' % len(diff))
        for i in diff:
            print('the %d is different' % i)
def test():
    file_name1 = input('please enter the first file name\n')
    file_name2 = input('please enter the second file name\n')
    compare(file_name1, file_name2)

def read(file_name, num):
    f = open(file_name)
    while num > 0:
        temp = f.readline()
        print(temp, end = '')
        num -= 1
def test():
    file_name = input('please enter the file name\n')
    num = int(input('which line'))
    print('文件：%s 前%d行内容为：\n' % (file_name, num))
    read(file_name, num)


def read(file_name, num):
    f = open(file_name)
    while num > 0:
        temp = f.readline()
        print(temp, end = '')
        num -= 1
def test():
    file_name = input('please enter the file name\n')
    num = int(input('which line'))
    print('文件：%s 前%d行内容为：\n' % (file_name, num))
    read(file_name, num)

def test():
    i = 0
    if i < 1:
        raise NameError("Invalid level!", i)

def test():
    A = 1
    B = 2
    print(locals())
    locals()

class Ball:
    def __init__(self, num):
        self.num = num
    def setNum(self, num):
        self.num = num

class Ticket:
    def __init__(self, weekend = False, child = False):
        if weekend == False:
            self.fee = 100
        else:
            self.fee = 120
        if child != False:
            self.fee *= 1/2
    def cal(self,num):
        return num * self.fee

import random as r
range_x = [0,10]
range_y = [0,10]

class Turtle:
    def __init__(self):
        self.power = 100
        self.x = r.randint(range_x[0], range_x[1])
        self.y = r.randint(range_y[0], range_y[1])
    def move(self):
        self.x = self.x + r.choice([-1,1,-2,2])
        self.y = self.y + r.choice([-1,1,-2,2])
        if self.x > range_x[1]:
            self.x = 2 * range_x[1] - self.x
        elif self.x < range_x[0]:
            self.x = 2 * range_x[0] - self.x
        if self.y > range_x[1]:
            self.y = 2 * range_y[1] - self.y
        elif self.y < range_x[0]:
            self.y = 2 * range_y[0] - self.y
        self.power -= 1
        return(self.x, self.y)
    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(range_x[0], range_x[1])
        self.y = r.randint(range_y[0], range_y[1])
    def move(self):
        self.x = self.x + r.choice([-1,1])
        self.y = self.y + r.choice([-1,1])
        if self.x > range_x[1]:
            self.x = 2 * range_x[1] - self.x
        elif self.x < range_x[0]:
            self.x = 2 * range_x[0] - self.x
        if self.y > range_x[1]:
            self.y = 2 * range_y[1] - self.y
        elif self.y < range_x[0]:
            self.y = 2 * range_y[0] - self.y
        return(self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if turtle.power == 0:
        print('turtle die')
        break
    if len(fish) == 0:
        print('no fish')
        break
    if turtle.move() == new_fish.move():
        pass


class Turtle:
    def __init__(self, x):
        self.num = x
class Fish:
    def __init__(self, x):
        self.num = x
class Pool:
    def __init__(self, x, y):
        self.fish = Fish(x)
        self.turtle = Trutle(y)
    def print_num(self):
        print('fish: %d\nturtle: %d' % (self.fish.num, self.turtle.num))

import math as m
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Line():
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()
        self.line_len = m.sqrt(self.x * self.x + self.y * self.y)
    def get_len(self):
        return self.line_len

class Duck():
    def walk(self):
        print('duck walking')
    def swim(self):
        print('duck swimming')

class Person():
    def walk(self):
        print('person walking')
    def swim(self):
        print('person swimming')

class Nstr(int):
    def __new__(cls, arg=0):
        total = 0
        for each in arg:
            total = +ord(each)
        arg = total
        return int.__new__(cls,arg)

def test():
    print('a')
    return test()

import time as t
class Mytimer:
    def start(self):
        print('time begins')
        self.begin = t.localtime()
    def stop(self):
        print('time is over')
        self.end = t.localtime()
        self.cal()
    def cal(self):
        self.sen = 'has spent'
        self.lasted = []
        for i in range(6):
            self.lasted.append(self.end[i] - self.begin[i])
            self.sen += str(self.lasted[i])
        print(self.sen)

class c:
    pass


class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.area = 0
    def __setattr__(self, name, value)
        if name == 'square':
            self.width = value
            self.height = value
        else:

    def get_area(self):
        return self.width * self.height

class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3

class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5

class Base:
    def test(self, x = 1):
        self.x = x
        print(self.x)

class A(Base):
    def test(self):
        super().test(x = 10)
        self.x = x
        print(self.x)

class B(Base):
    def test(self):
        super().test()
        print('B')

class C(A,B):
    def test(self):
        super().test()
        print('C')

class Base:
    def test(self, x = 1):
        self.x = x
        print(self.x)

class A(Base):
    def test(self,x):
        super().test(x = 10)
        self.x = x
        print(self.x)

class C:
    def get1(self):
        return 100
    x = property(get1)

class C:
    def __init__(self, d = 26):
        self.d = float(d)

    def __get__(self, instance, owner):
        return self.d

    def __set__(self, instance, d):
        self.d = float(d)

class F:
    def __get__(self, instance, owner):
        return instance.c * 1.8 + 12

    def __set__(self, instance, owner):
        instance.c = (float(d)-12)/1.8

class Temp:
    c = C()
    f = F()

import tkinter as tk
root = tk.Tk()
root.title('i am your father')
l = tk.Label(root, text = 'hi, my name is marcus')
l.pack()
root.mainloop()

class Test:
    b = 200
    def __init__(self):
        self.a = 100

def test(x):
    print(x)
    def test2():
        x = 100
        print(x)
    test2()
    print(x)

def test(x, y):
    x + y