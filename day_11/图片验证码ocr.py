import tesserocr
from PIL import Image
import numpy as np
import time
import re
from selenium import webdriver
from io import BytesIO
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from retrying import retry


def preprocess(image):
    image = image.convert('L')
    data = image.getdata()
    w, h = image.size
    count = 0
    for x in range(1, h - 1):
        for y in range(1, h - 1):
            # 找出各个像素方向
            mid_pixel = data[w * y + x]
            if mid_pixel == 0:
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]

                if top_pixel == 0:
                    count += 1
                if left_pixel == 0:
                    count += 1
                if down_pixel == 0:
                    count += 1
                if right_pixel == 0:
                    count += 1
                if count > 4:
                    image.putpixel((x, y), 0)
    image.show()
    return image


@retry(stop_max_attempt_number=10, retry_on_result=lambda x: x is False)
def login():
    browser.get('https://captcha7.scrape.center/')
    browser.find_element_by_css_selector('.username input[type="text"]').send_keys('admin')
    browser.find_element_by_css_selector('.password input[type="password"]').send_keys('admin')
    captcha = browser.find_element_by_css_selector('#captcha')
    image = Image.open(BytesIO(captcha.screenshot_as_png))
    image = preprocess(image)
    captcha = tesserocr.image_to_text(image)
    captcha = re.sub('[^A-Za-z0-9]', '', captcha)
    print(captcha)
    browser.find_element_by_css_selector('.captcha input[type="text"]').send_keys(captcha)
    browser.find_element_by_css_selector('.login').click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(.,"登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False


if __name__ == '__main__':
    browser = webdriver.Chrome()
    login()
