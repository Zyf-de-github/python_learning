import requests
import random



# url="https://www.baidu.com"
#
# response=requests.get(url)
# print(response)
# # print(response.text)
# print(response.content.decode('utf-8'))
# with open("test.html","w",encoding="utf-8") as f:
#     f.write(response.content.decode('utf-8'))

# url="https://gips0.baidu.com/it/u=1690853528,2506870245&fm=3028&app=3028&f=JPEG&fmt=auto?w=1024&h=1024"
# res=requests.get(url)
# print(res.content)
# with open("test.jpg","wb") as f:
#     f.write(res.content)
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# # """with open("test.jpg","wb") as f:  作用等同于 try-except-finally 语句，用于处理文件读写异常"


# #需要添加user-agent，否则会被识别为爬虫
# url="https://www.baidu.com"
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
# }
# response1=requests.get(url,headers=headers)
# response2=requests.get(url)
#
# print(response1.content.decode())
# print(len(response1.content.decode()))
# print(len(response2.content.decode()))



# ###添加请求池防止反爬
# ###多个uesr-agent，随机选择一个
#
# UA_LIST = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
#     'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/137.0.0.0',
#     'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/137.0.0.0'
#     ]
# #或者使用fake-useragent库
# #使用假的user-agent
#
# # print(random.choice(UA_LIST))
# # headers = {'User-Agent': random.choice(UA_LIST)}
#
#
#
#
# """在浏览器搜索关键字时，会经历从明文转变为密文的过程"""
# """%E5%AD%A6%E4%B9%A0 转变为 学习"""
# """明文转密文的模块叫做：quote、unquote\
# from urllib.parse import quote,unquote
#
# """
# from urllib.parse import quote,unquote
# print(quote("学习"))
# print(unquote("%E5%AD%A6%E4%B9%A0"))
#
# ##### 带参数的请求
# #####1、通过params参数传递参数


# url="https://www.baidu.com/s"
# UA_LIST = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
#     'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/137.0.0.0',
#     'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/137.0.0.0',
#     # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'
#     ]
# keyword=input("请输入搜索关键字：")
# params={
#     'wd':keyword,
# }
# headers = {'User-Agent': random.choice(UA_LIST)}
# res=requests.get(url,headers=headers,params=params)
# print(res.content.decode())
#
# ###2、直接携带参宿
# name=input()
# url=f"https://www.baidu.com/s?wd={name}"
