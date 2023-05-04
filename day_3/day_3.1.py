from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener, ProxyHandler
from urllib.error import URLError

username = "admin"
password = "admin"
url = "https://ssr3.scrape.center/"

# proxy_handler = ProxyHandler({
#     "http": "http://127.0.0.1:8080",
#     "https": "https://127.0.0.1:8080"
# })

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("UTF-8")
    print(html)
except URLError as e:
    print(e.reason)
