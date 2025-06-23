
# class complex_function():
#     def __init__(self,a,b):
#         self.real = a
#         self.imag = b
#     def my_print(self):
#         print('(',self.real,',',self.imag,'j)')
#
#
#
# c=complex_function(3,4)
# d=complex_function(5,-8)
# c.my_print()
# d.my_print()


# class person:
#     name=''
#     age=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def speak(self):
#         print("Hello, my name is",self.name,"and I am",self.age,"years old.")
#
#
# class student(person):
#     num=0
#     def __init__(self,name,age,num):
#         person.__init__(self,name,age)
#         self.num=num
#     def speak(self):
#         print("Hello, my name is",self.name,"and I am",self.age,"years old. I am a student and my student number is",self.num)
#
# class teacher(person):
#     subject=''
#     def __init__(self,name,age,subject):
#         person.__init__(self,name,age)
#         self.subject=subject
#     def speak(self):
#         print("Hello, my name is",self.name,"and I am",self.age,"years old. I am a teacher and my subject is",self.subject)
#
# class speaker:
#     name=''
#     topic=''
#     def __init__(self,name,topic):
#         self.name=name
#         self.topic=topic
#     def showtime(self):
#         print("Hello, my name is",self.name,"and I am a speaker. My topic is",self.topic)
#
# class student_speaker(student,speaker):
#     def __init__(self,name,topic,age,num):
#         student.__init__(self,name,age,num)
#         speaker.__init__(self,name,topic)
#
#
#
# # s1=student('ken',14,282873)
# # t1=teacher('john',25,'math')
# # s1.speak()
# # t1.speak()
# show1=student_speaker('jane','math',16,282874)
# show1.showtime()
# show1.speak()



# def hcf(a,b):           # function to find hcf of two numbers
#     data,small=0,0
#     if a>b:
#         small= b
#     else:
#         small= a
#
#     for i in range(small,0,-1):
#         if a%i==0 and b%i==0:
#             data= i
#             break
#
#     return data
#
# print(hcf(6,36))
# print(hcf(5,7))
# print(hcf(18,27))
# print(hcf(6,9))
# print(hcf(4,6))


# def lcm(a,b):
#     great,data=0,0
#     if a>b:
#         greater=a
#         data=greater
#     else:
#         greater=b
#         data=greater
#
#     while(True):
#         if data%a==0 and data%b==0 :
#             return data
#         else:
#             data=data+1
#
#
# print(lcm(12,24))
# print(lcm(5,7))
# print(lcm(7,36))
# print(lcm(5,5))
# print(lcm(1,7))


def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


# while True:
#     print("1.add")
#     print("2.subtract")
#     print("3.multiply")
#     print("4.divide")
#     print("0.exit")
#
#     print("please enter your choice==>")
#     choice=int(input())
#     if choice!=0:
#         print("please enter your first num==>")
#         a=int(input())
#         print("please enter your first num==>")
#         b=int(input())
#     if choice==1:
#         print(add(a,b))
#     elif choice==2:
#         print(subtract(a,b))
#     elif choice==3:
#         print(multiply(a,b))
#     elif choice==4:
#         print(divide(a,b))
#     elif choice==0:
#         print("exiting...")
#         break
#     else:
#         print("invalid choice, please try again")


# x,a,data=0,1,0
# while True:
#     x=a
#     a+=1
#     for i in range(1,6):
#         data=5*x/4+1
#         x=data
#     if data%1==0:
#         break
#
# print(data)


# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(0))





