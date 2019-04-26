import requests
#URL管理
#网页下载
#网页解析
#输出管理
#构造请求头

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36'}

#HTTP请求、超时设置、URL，get方法
url = 'https://www.douban.com/'
#response = requests.get('https://www.douban.com/')
response = requests.get(url,headers = headers,timeout = 3)

#   ’get‘的位置 也可以用 post ,put,delete,head,options等

print(response.encoding)   #编码方式
#print(response.content)    #网页源码
print(response.status_code)#状态码
print( response.status_code == requests.codes.ok)
#request内置状态码查询

#输出请求头
print(response.request.headers)
#字典形式的请求头输出
print(response.headers)


#重定向
r= requests.get('http://www.douban.com')
print(r.history)
#查看实时请求的URL
print(r.url)


