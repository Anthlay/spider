import requests
from bs4 import BeautifulSoup
def get_movies():
    headers={#中间用逗号隔开
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.3.16721',
    'Host':'movie.douban.com'
 }
    movie_list=[]
    for i in range(0,20):#记住冒号不能丢
     link='https://movie.douban.com/top250?start='+str(i*25)
     r=requests.get(link,headers=headers,timeout=20)
     print(str(i+1),"页响应状态码",r.status_code)

     #print(r.text)
    soup=BeautifulSoup(r.text,"lxml")
    div_list=soup.find_all('div',class_='hd')
    for each in div_list:
        movie=each.a.span.text.strip()
        movie_list.append(movie)
        return movie_list
movies=get_movies()
print(movies)
#get_movies()跳