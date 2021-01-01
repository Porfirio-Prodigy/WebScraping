#Web Scraping
import requests
import json
from bs4 import BeautifulSoup

entrada = input('Site: ')
res = requests.get("http://"+entrada)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find_all(class_='widgets-list-layout-links')

all_posts = []
for post in posts:
    info = post.find(class_="widgets-list-layout-links")
    title = post.find('a').text
    links = post.find('a')['href'] 
    
    all_posts.append({
        'title': title,
        'links': links
    })
    
#print(all_posts)
with open('posts.json', 'w') as json_file:
    json.dump(all_posts, json_file, indent=3, ensure_ascii=False)

