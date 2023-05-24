from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def parse_name(name_html):
    soup = BeautifulSoup(name_html, 'lxml')
    has_whole = soup.find(attrs={'class': 'whole'})
    if has_whole:
        return has_whole.text
    else:
        chars = soup.find_all(attrs={'class': 'char'})
        items = []
        for char in chars:
            left_value = char['style'].split('left:')[1].strip(';').strip()
            left_num = int(left_value[:-2])
            items.append({
                'text': char.text.strip(),
                'left': left_num
            })
        items = sorted(items, key=lambda x: x['left'], reverse=False)
        return ''.join([item.get('text') for item in items])


browser = webdriver.Chrome()
browser.get('https://antispider3.scrape.center/')
WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item')))
html = browser.page_source
names = browser.find_elements_by_class_name('name')
for name in names:
    name_html = name.get_attribute('outerHTML')
    name_final = parse_name(name_html)
    print(name_final)

browser.close()
