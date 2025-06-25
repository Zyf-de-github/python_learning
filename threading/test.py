import queue
import threading
import time

# class MyThread(threading.Thread):
#     def __init__(self,threadID,name,detime):
#         threading.Thread.__init__(self,name=name)
#         self.threadID = threadID
#         self.name = name
#         self.detime = detime
#     def run(self):
#         print("Starting " + self.name)
#         print_time(self.name,self.detime,counter=5)
#         print("Exiting " + self.name)
#
#
#
# def print_time(name,detime,counter):
#     for i in range(counter):
#         time.sleep(detime)
#         print ("%s: %s" % (name, time.ctime(time.time())))
#
# thread1=MyThread("thread1",name="thread1",detime=1)
# thread2=MyThread("thread2",name="thread2",detime=2)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Exiting Main Thread")


# """全局变量定义"""
# a=0
# c=0
# b=1000000
# d=500000
#
# lock1=threading.Lock()#创建互斥锁
# lock2=threading.Lock()#创建互斥锁
# lock3=threading.Lock()
#
#
# def add1():
#     global a
#     lock1.acquire()#获取锁
#     for i in range(b):
#         a=a+1
#     lock3.acquire()
#     print('first:',a)
#     lock3.release()
#     lock1.release()#释放锁
#
# def add2():
#     global a
#     lock1.acquire()#获取锁
#     for i in range(b):
#         a=a+1
#     lock3.acquire()
#     print('second:',a)
#     lock3.release()
#     lock1.release()#释放锁
#
# def add3():
#     global c
#     lock2.acquire()#获取锁
#     for i in range(d):
#         c=c+1
#     lock3.acquire()
#     print('first:',c)
#     lock3.release()
#     lock2.release()#释放锁
#
# def add4():
#     global c
#     lock2.acquire()#获取锁
#     for i in range(d):
#         c=c+1
#     lock3.acquire()
#     print('first:',c)
#     lock3.release()
#     lock2.release()#释放锁
#
# if(__name__=="__main__"):
#     t1=threading.Thread(target=add1)
#     t2=threading.Thread(target=add2)
#     t3=threading.Thread(target=add3)
#     t4=threading.Thread(target=add4)
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()


import queue


# q=queue.Queue(3)
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.empty())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())


"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
"""精华精华"""
"""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
# """多任务，数据的共享写入和读取"""
# """"""""""""""""""""""""""""""
# import collections  #外部引用队列
#
#
# lock1=threading.Lock()#创建互斥锁
#
# li=collections.deque([1,2,3,4,5,6,7,8,9,10])
#
# def wdata(q):
#     global li
#     while True:
#         lock1.acquire()
#         if not q.full():
#             if len(li):
#                 item=li.popleft()
#                 print('wdata : put data',item,'\n')
#                 q.put(item)
#             else:
#                 print('wdata : li is empty, wait for data\n')
#         else:
#             print('wdata : data is full\n')
#         lock1.release()
#         time.sleep(0.5)
#
# def rdata(q):
#     global li
#     while True:
#         lock1.acquire()
#         if not q.empty():
#             print('rdata : get data',q.get(),'\n')
#         else:
#             print('rdata : data is empty\n')
#         lock1.release()
#         time.sleep(1)
#
# if __name__ == '__main__':
#     q=queue.Queue(3)
#     t1=threading.Thread(target=wdata,args=(q,))
#     t2=threading.Thread(target=rdata,args=(q,))
#     t1.start()
#     t2.start()
#
#     # item=li.popleft()
#     # print('item is ',item)


# def tesk1():
#     yield 'hhh'
#     yield 'hahaha'
#
# def tesk2():
#     yield 'bbb'
#     yield 'bababa'
#
# def tesk3():
#     while True:
#         yield 'bks'
#         yield 'aks'
#
# if __name__ == '__main__':
#     t1=tesk1()
#     t2=tesk2()
#     t3=tesk3()
#     print(next(t1))
#     print(next(t2))
#     print(next(t1))
#     print(next(t2))
#     while True:
#         print(next(t3))
#         time.sleep(1)



#gevent   自动切换协程  耗时操作
#monkey补丁

#greenlet   手动切换协程