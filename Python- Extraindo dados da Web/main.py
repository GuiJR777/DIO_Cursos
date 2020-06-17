import requests
from bs4 import BeautifulSoup

res= requests.get('https://www.tudocelular.com/')
res.encoding='utf-8'

soup= BeautifulSoup(res.text, 'html.parser')

posts= soup.find_all(class_='newlist_normal')

all_posts=[]
for post in posts:
    info= post.find(class_='title_newlist_normal')
    title=info.a.text

    
    print(title)

# print(posts[0])