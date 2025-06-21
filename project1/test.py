# print("hello world")


# str = "abcdefghijklmnopqrst"
# print(str[0:5]) # prints "abcde"
# print(str[5:10]) # prints "fghij"
# print(str[10:-1])
# print(str[0:])
# print(str[10:])
# print(str+"你好")
# print(str*2)


# input("\n\n按下 enter 键后退出。")
# str = "abcdefghijklmnopqrst"
# print(str[0:5]) # prints "abcde"


# import sys; x = 'runoob'; sys.stdout.write(x + '\n')


# 变量="变量"
# print(变量)
# 姓名 = "张三"  # 合法
# π = 3.14159   # 合法





##############    list[]列表   tuple()元组   set{}集合  dict{}字典   #
# list54 = ['abcde',57,36.3,'张飞',2+2j]            #列表的元素可以改变
# print(list54[0:-4])
# print(list54[-5:-1])
# list54[1:3]=[111,999]
# print(list54)
# print(list54[::2])
# print(list54[::-2])
# print(list54[0::-2])
# print(list54[2::-2])
# print(list54[-1::-2])
# list54=list54[-1::-1]
# print(list54)
# list54[1]='赵云'
# print(list54)
#
# list1=(1,2,3,4,5)        #元组的元素不能改变
# #list1[0]=12
# #print(list1)   #error

# c={'abc','def','ghi','ghi','abc'}           #集合的元素不能重复
# d={'abc','ghi'}
# print(c)            #自动去重
# print(d)
# print("差集：",end='')
# print(c-d)
# print("并集：",end='')
# print(c|d)
# print("交集：",end='')
# print(c&d)
# print("不同时存在的元素：",end='')
# print(((c|d)-(c&d)),end='')              #   ==a^b
# print(c^d)
#
#
#
# a=set('abcd')
# b=set('cdef')
# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)


# my_dict={'name':'张三','age':25,'gender':'男'}
# # print(my_dict.get('name'))
# # print(my_dict.keys())
# # print(my_dict.values())
# # print(my_dict.items())
# print(my_dict)
#
# dict={}
# dict['name']='张三'
# dict['age']=10
# dict['tele']=222222222
# print(dict)
# print(dict['name'])
# print(dict['tele'])
# print(dict['age'])

# x = bytes("hello", encoding="utf-8")
# print(x)
# x = b"hello"
# if x[0] == ord("h"):
#     print("The first element is 'h'")


"""
这是多行注释
adsad啦啦啦
撒大大
)
"""


# num = 10
# print(num)
# del num
# print(num)

# a=complex(1,2)
# print(a)


# import math
# print(max(1,2,3,4,5))
# print(math.sqrt(25))
# print(math.exp(2))

# !/usr/bin/python3

# var1 = 'Hello World!'
# print("已更新字符串 : ", var1[:6] + 'Runoob!')
# print("已更新字符串 : ", var1[:0] + 'Runoob!')
# print("\a")

# import time
#
# for i in range(101): # 添加进度条图形和百分比
#     bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
#     print(f"\r{bar} {i:3}%", end='')#, flush=True)
#     time.sleep(0.05)
# print()

# a="""
#     This is a test of the emergency broadca
# -st system
#     Just like an English ababababbababababa
# and so on and so forth
#                             Bast wish for you
#                                 Yours Truly,
# """
# print(a)

# for num in range(10):
#     print(num,end='')
# while True:
#     pass

# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)

# tuple1=(1,2,3)
# print(len(tuple1))
# tuple2=('012345','abcde','aihsia')
# print(tuple2[0][3],tuple2[2][1],tuple2[1][0])
dict1={'name':'zhangsan','age':18}
print(dict1['name'])
print(len(dict1))
