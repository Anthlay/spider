#名副其实，真特么慢【-—_--】
import requests
import re
from bs4 import BeautifulSoup as bs
from lxml import etree
link1 = "http://www.santostang.com/"
link2 = "http://www.6vhao.tv"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}

#爬6v电影
r = requests.get(link2,headers=headers)
print(r.encoding)
r.encoding = 'gb2312'#使编码一致,不出现乱码
soup = bs(r.text,"html.parser")#创建bs对象


#for i in soup.select("aside > body.u1"):
#print(soup.select("li a"))
#list_sl = soup.select("li a")#逐层查找
#print(list_sl)
#str1 = "".join(list_sl)#列表转化为字符串//有误
#print(re.findall('>.*?(.*?)'),str1)

name_movie = soup.find("div",class_="channeltype").a.text.strip()
print(name_movie)
name_allmovie = soup.find_all("div",class_="channeltype")
for i in range(len(name_allmovie)):
    print(name_allmovie[i+1].a.text.strip())
   # String nm += name_allmovie[i+1].a.text.strip()


print(re.findall('title=".*?(.*?)">',name_allmovie))





#基础语法
'''
r = requests.get(link1,headers=headers)
soup = bs(r.text,"html.parser")#转化成BS对象
#遍历文档树部分
print(soup.head.meta)
print(soup.title)#+1
'''

'''
print(soup.style.contents)#子节点
print(soup.style.contents[1])
for child in soup.style.children:#获取所有子标签
    print(child)
for child in soup.style.descendants:#获取所有子子孙孙标签
    print(child)
print(soup.meta.parent)#获取父节点
    '''

'''
搜索文档树部分
for tag in soup.find_all():#输出所有标签
    #print(tag.name)
for tag in soup.find_all(re.compile("^l")):#输出所有l开头的标签,可以高效地理清标签结构
    print(tag.name)
'''

'''
#css选择器部分
#print(soup.select("div p"))#逐层查找，筛选文字非常有用
print(soup.select("aside > h4 "))#子标签直接遍历
print(soup.select('link[href^="http://www"]'))#使用搜索树功能

'''




'''
first_title = soup.find("h1",class_="post-title").a.text.strip()
print("第一篇文章的标题："+first_title)

title_list = soup.find_all("h1",class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print(i+1, title)
'''