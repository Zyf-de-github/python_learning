import requests
import random

# #保存图片示例
# # 1.打开浏览器，访问易云音乐图片地址
# url='https://p1.music.126.net/XrLZ9hcDXg4FfG47NAtfeg==/109951171359057225.jpg?imageView&quality=89'
# # 2.复制url地址，并在代码中粘贴
# UA_LIST = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
#     'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/137.0.0.0',
#     'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/137.0.0.0'
#     ]
#
# # 3.设置请求头，随机选择一个UA
# headers = {'user-agent': random.choice(UA_LIST)}
# res=requests.get(url,headers=headers)
# # print(res.content.decode())
#
# # 4.保存图片,以二进制方式写入文件
# with open('网易云.jpg','wb') as f:
#     f.write(res.content)


# #保存音乐
# url='https://m804.music.126.net/20250626220001/516b137b8af9b91934a8333a02e1fad4/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/45350745514/87a0/e81f/1b04/5415394535e0ab438f32e9330e19bacd.m4a?vuutv=1tiLgurQaSYB5dF+Pj/z5Z0uOmmV/7A5tOZYb4lIAU4O855Hpm8ZbNEs80pJ5rKvjiQa8dIDxrv0Jn8BW2jdFo662BFnc7MGaVT9Ey0YUp8=&authSecret=00000197ac72e9d31e990a3084390c08'
#
# UA_LIST = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
#     'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/137.0.0.0',
#     'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 CrKey/1.54.248666 Edg/137.0.0.0'
#     ]
#
# headers = {'user-agent': random.choice(UA_LIST)}
# res=requests.get(url,headers=headers)
# # print(res.content)
#
# with open('大展宏图.mp3','wb') as f:
#     f.write(res.content)

