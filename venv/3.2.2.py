import requests

from lxml import etree
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36'}

#HTTP请求、超时设置、URL，get方法
url = 'https://www.douban.com/'
#response = requests.get('https://www.douban.com/')
response = requests.get(url,headers = headers,timeout = 3)
htm = response.content

selector = etree.HTML(htm)

all_li = selector.xpath('//div/ul/li/a/@class[1]')
print(all_li)