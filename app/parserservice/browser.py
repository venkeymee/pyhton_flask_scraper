import os
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen

# options = webdriver.ChromeOptions()
# desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# options.add_argument('headless')
# browser = webdriver.Chrome(options= options,desired_capabilities= desired_capabilities)


class Browser:
    def __init__(self):
        print("init")
        # A normal print function

    def get_browser(self,main_url):
        try:
            f = urlopen(main_url)
            html_content = f.read()
        except Exception as e:
            print(e)
        return BeautifulSoup(html_content, 'lxml')

    def get_detailpage(url):
        try:
            browser.get(url)
        except Exception as a:
            print(a)
        return BeautifulSoup(browser.page_source, 'html.parser')
