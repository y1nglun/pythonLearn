import requests
from selenium import webdriver

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


options = webdriver.ChromeOptions()
print(get_proxy())
options.add_argument('--proxy-server=http://' + get_proxy())
browser = webdriver.Chrome(options=options)
browser.get('http://www.httpbin.org/get')
print(browser.page_source)

