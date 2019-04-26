encoding: 'UTF-8'
#正则表达式真他妈没意思@
#部分内容已可保存到txt
import requests
import os
import re
link1 = r"http://www.baidu.com"
link2 = r"http://www.qidian.com"
link21= r"https://www.qidian.com/rank?chn=21"
link3 = r"http://www.santostang.com"
link4 = r"http://movie.douban.com/top250"
link5 = r"http://www.6vhao.tv"
path_baidu  =  "G:/mycode/baidu.txt"
path_qidian = "G:/mycode/qidian.txt"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}
'''
r = requests.get(link5,headers = headers)

print(r.encoding)
r.encoding = 'gb2312'
html = r.text
list_HTTP = re.findall("https://.*?com",html)

#list_nname = re.findall('target="_blank">.*?(.*?)</a></li>',html)#括号里的重复部分表示只选择缺失部分
list_nname = re.findall('target=_blank>.*?(.*?)</a>&nbsp;',html)#括号里的重复部分表示只选择缺失部分
print(list_nname)
for i in range(list_nname):
    print(list_nname[i+1])
    print()

'''
'''
#豆瓣top250，数据是脏的。。电影名没法保存，还不能翻页
path_baidu  =  "G:/mycode/baidu.txt"
path_qidian = "G:/mycode/qidian.txt"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721'}
r = requests.get(link4,headers = headers)

print(r.encoding)
html = r.text
list_HTTP = re.findall("https://.*?.com",html)
print('get所有的网址：')
print(list_HTTP)
print()

list_nname = re.findall('<span class="title">.*?(.*?)</span>',html)#括号里的重复部分表示只选择缺失部分
print(list_nname)
print()


'''

#唐松博客
r = requests.get(link5,headers = headers)
html = r.text
list_HTTP = re.findall("https://.*?.com",html)
print('get所有的网址：')
print(list_HTTP)
print()
list_nname = re.findall('le">.*?(.*?)</h4>',html)#括号里的重复部分表示只选择缺失部分
print(list_nname)
print()

#写入TXT
'''
output = '\t'.join(list_nname)#因为数据不干净，有乱码，故保存不进去


#output = '\t'.join(list_HTTP)

with open(u'G:/mycode/baidu.txt',"a+") as f:
    f.write(output)
    f.close()
'''
