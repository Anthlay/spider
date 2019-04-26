import requests
from bs4 import BeautifulSoup
import os
import re

Hostreferer = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721',
    'Referer':'http://www.mzitu.com'
}
Pircreferer = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721',
    'Referer':'http://i.meizitu.net'
}

def get_page_name(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    span = soup.findAll('span')
    title = soup.find('h2',class_="main-title")
    return span[10].text,title.text

def get_html(url):
    req = requests.get(url,headers=Hostreferer)
    html = req.text
    return html

def get_img_url(url, name):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    img_url = soup.find('img',alt=name)
    return img_url('src')

def save_img(img_url,count,name):
    req = requests.get(img_url,headers=Pircreferer)
    with open(name+'/'+str(count)+'.jpg','wb') as f:
        f.write(req.contrnt)

def main():
    old_url = "http://www.mzitu.com/123114"
    page, name = get_page_name(old_url)
    os.mkdir(name)
    for i in range(1,int(page)+1):
        url = old_url+"/"+str(i)
        img_url = get_img_url(url,NameError)
        save_img(img_url,i,name)
        print('保存第'+str(i)+'张图片成功')

main()