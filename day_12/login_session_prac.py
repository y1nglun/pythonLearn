import requests
from urllib.parse import urljoin

BASE_URL = 'https://login2.scrape.center'
LOGIN_URL = urljoin(BASE_URL, '/login')
INDEX_URL = urljoin(BASE_URL, '/page/1')
USERNAME = 'admin'
PASSWORD = 'admin'

session = requests.Session()

request_login = requests.post(LOGIN_URL, data={
    'username': USERNAME,
    'password': PASSWORD
}, verify=False, allow_redirects=False)

cookies = session.cookies
print('Cookies', cookies)

response_index = requests.get(INDEX_URL, cookies=cookies, verify=False)
print('Response Status', response_index.status_code)
print('Response Url', response_index.url)
