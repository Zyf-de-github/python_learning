import requests



url="https://www.baidu.com"

response=requests.get(url)
print(response)
# print(response.text)
print(response.content.decode('utf-8'))
with open("test.html","w",encoding="utf-8") as f:
    f.write(response.content.decode('utf-8'))

# url="https://gips0.baidu.com/it/u=1690853528,2506870245&fm=3028&app=3028&f=JPEG&fmt=auto?w=1024&h=1024"
# res=requests.get(url)
# print(res.content)
# with open("test.jpg","wb") as f:
#     f.write(res.content)
# #""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# # """with open("test.jpg","wb") as f:  作用等同于 try-except-finally 语句，用于处理文件读写异常"