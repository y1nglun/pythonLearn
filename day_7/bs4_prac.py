import re

from bs4 import BeautifulSoup

"""
方法选择器
"""
with open('test2.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.section.p.attrs['class'])
    print(soup.section.contents[1].string)
    for ul in soup.find_all(name='ul'):
        for li in ul.find_all(name='li'):
            print(li.string)

    print(soup.find_all(attrs={'id': 'ul1'}))
    print(soup.find_all(attrs={'name': 'ol1'}))
    print(soup.find_all(string=re.compile('Blog')))
"""
CSS选择器
"""
print(soup.select('.foot'))
print(soup.select('ul li'))
print(soup.select('#ul1 .css'))
for ul in soup.select('ul'):
    print(ul['id'])
