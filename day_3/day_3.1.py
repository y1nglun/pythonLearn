import os

import requests
from bs4 import BeautifulSoup

movie_list = []
save_path = "豆瓣电影"
path = save_path + "/" + "TOP250.txt"

for page in range(0, 250, 25):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36"
    }
    response = requests.get(f"https://movie.douban.com/top250?start={page}", headers=headers)
    if response.ok:
        content = response.text
    else:
        print(response.status_code)

    soup = BeautifulSoup(content, "html.parser")
    all_title = soup.findAll("span", attrs="title")
    for title in all_title:
        title_string = title.string
        if '/' not in title_string:
            print(title_string)
            movie_list.append(title_string)

print(movie_list)

if not os.path.exists(save_path):
    os.mkdir(save_path)
with open(path, "w+", encoding="utf-8") as fp:
    for i in movie_list:
        fp.write(str(i) + '\n')
