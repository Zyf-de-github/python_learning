from collections import deque

# while True:
#     age = int(input("enter your age:"))
#
#     if age<0 and age!=-999:
#         print("age is less than zero")
#     elif age>=0 and age<18:
#         print("age is ",age)
#     elif age>=18 and age<80:
#         print("you are so old , age is ",age)
#     elif age>80:
#         print("you are so so old , age is ",age)
#     else:
#         break


# a,b=1,0
# for x in range(10):
#     a,b=b,a+b
#     print(a,end=" ")


# a='abcd'
# print(len(a))
# name=['tom','bob','marry','edgar','allfer']
# name3=[a for a in name if len(a)<=3]
# print(name3)

# num=[a for a in range(40) if( a%5==0 and a%10!=0 )or a%20==0]
# print(num)

# namelist=['tom','bob','marry','edgar','allfer']
# namedict={len(a):a for a in namelist }
# print(namedict)             # 字典的键是字符串的长度，值是字符串本身，字典的键值对是无序的，当有两个相同的键时，前一个元素会被后一个元素覆盖


# strings='ajsixsjbduwdushnxaisjdihwdskcoaskxoskaoxwxhacfdcnxi'
# ### a={a: for a in strings if a=='a' or a=='b' or a=='c' or a== 'd'}  #error
# a=strings.count('a')
# print(a)
# cahrtimes={x:strings.count(x) for x in strings if x in ['a','b','c','d']}  #right
# print(cahrtimes)

# print(i=range(10))
# for i in range(10):
#     print(i,end=' ')

# def print_hello():
#     print('hello world')
#
# def max_out(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
#
# print_hello()
# a=3
# b=5
# print(max_out(a,b))


# def change(a):
#     print(id(a))  # 指向的是同一个对象
#     a = 10
#     print(id(a))  # 一个新对象
#     print(a)
#
# a=1
# print(id(a))
# change(a)       #还是有形参和实参的区别
# print(id(a))
# print(a)

# dev=lambda x,y:x/y
# sum=lambda a,b:a+dev(a,b)
# print(sum(1,2))
# print(sum(5,6))


# import time
#
# def test(func):             #固定用法
#     def x():
#         print('start')
#         func()
#         print('finish')
#     return x
#
# @test
# def time_show():
#     print(time.ctime())
#
# @test
# def data_show():
#     print("absabsdba")
#
# @test
# def password_show():
#     print("123456")
#
#
# time_show()
# data_show()
# password_show()



# def deco(func):
#     def wrapper(*args, **kwargs):
#         print('brfore')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
#
# @deco
# def test1(a):
#     print(a)
#
# @deco
# def test2(a,b):
#     print(a,b)
#
# @deco
# def test3(a,b,c):
#     print(a,b,c)
#
# test1('aaa')
# test2('aaa','bbb')
# test3('aaa','bbb','ccc')


# func(str)         #必要参数
# func(str='abc',num=10)   #关键字参数 函数可以自己匹配，可以先定义str后定义num，也可以先定义num后定义str
                           #默认参数也是这样写
#func(*str,**num)   #*表示元素按照元组的形式传入，**表示元素按照字典的形式传入，可用于不定长参数的函数调用

# def deco(func):
#     def wrapper(*args, **kwargs):
#         print('brfore')
#         func(*args, **kwargs)
#         print('after')
#     return wrapper
# """
# wrapper(*args, **kwargs): 这一行代码定义了装饰器函数 deco
# 中的一个内部函数 wrapper，它接受任意数量的位置参数（*args）和关
# 键字参数（**kwargs）。在装饰器中，*args 和 **kwargs 被用来传
# 递被装饰函数 func 的原始参数，使得 wrapper 可以在不改变函数签名
# 的情况下，对函数调用进行前后处理。
# """


# stack1=[]
# print(stack1)
# stack1.append(1)
# print(stack1)
# stack1.append(2)
# print(stack1)
# stack1.append(3)
# print(stack1)
# print(stack1.pop())
# print(stack1.pop())
# print(stack1.pop())

# queue1=deque()#双端队列  使用popleft出栈
# #使用列表也可以实现队列，但队列的操作效率更高 使用pop(0)和append(0)方法


##队列表达式
# stack1=[1,2,3,4,5]
# stack1=[3*x for x in stack1]
# print(stack1)
# stack1=[[3*x,x**2] for x in stack1]
# print(stack1)

# import support
# # support.support()
#
# def print_location():
#     print(f"模块的 __name__ 值: {__name__}")
#
#
# if(__name__=="__main__"):
#     # print("the main is running")
#     # support.hello()
#     support.print_location()
#     print_location()
# else:
#     print("the main is not running, the support is running")



# x = 6
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))








num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    # print(num)
    num = 123
    # print(num)

print(num)
fun1()
print(num)

