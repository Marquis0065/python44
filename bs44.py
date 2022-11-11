from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# path = Service('chromedriver.exe')

# brower = webdriver.Chrome(service=
browser = webdriver.Chrome('chromedriver.exe')
browser.get('http://jd.com')
