from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_home_e2e_headless():
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')   # use '--headless=new' for latest versions
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get('http://127.0.0.1:5000/')
        time.sleep(1)
        assert 'Flask API Running Successfully' in driver.page_source
    finally:
        driver.quit()
