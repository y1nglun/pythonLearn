import requests
import configparser


def create_session():
    cf = configparser.ConfigParser()
    cf.read('config.ini')
    cookies = cf.items('cookies')
    cookies = dict(cookies)
    from pprint import pprint
    pprint(cookies)
    phone = cf.get('info', 'phone')
    password = cf.get('info', 'password')

    session = requests.session()
    login_data = {'phone': phone, 'password': password}
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36"
    }
