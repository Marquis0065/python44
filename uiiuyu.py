import urllib.request
import urllib.parse
from lxml import etree
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
path = Service('chromedrive.exe')
browser = webdriver.Chrome(service=path)
browser.get('http://www.baidu.com')
