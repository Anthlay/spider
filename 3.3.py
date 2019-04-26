#爬取百度首页“新闻”和其链接

import requests
from lxml import etree

response = requests.get('http://www.baidu.com/')
response.encoding = 'utf-8'

selector = etree.HTML(response.text)
print(selector)