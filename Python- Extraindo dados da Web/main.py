import requests
from bs4 import BeautifulSoup

res= requests.get('https://www.telelistas.net/sc/florianopolis/igrejas+templos+e+instituicoes+religiosas')
res.encoding='utf-8'

soup= BeautifulSoup(res.text, 'html.parser')

posts= soup.find_all(class_="q-card__section q-card__section--vert")

all_posts=[]
for post in posts:
    info= post.find(class_="cheader cursor-pointer")
    title= info.h3.text
    print(title)

# print(len(posts))