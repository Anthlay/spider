import requests
#查询字符串
payload = {'q':'python','cat':'1001'}

r=requests.get('https://www.douban.com/search',params=payload)

print(r.url)