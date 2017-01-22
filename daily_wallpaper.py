from bs4 import BeautifulSoup as bs
import requests as req
from selenium import webdriver
import time
import random
from time import sleep
url = 'https://www.pexels.com/search/abstract/'
# url = 'https://www.pexels.com/search/HD%20wallpaper'
b = webdriver.Chrome('/home/vbshah/chromedriver')
b.get(url)
# time.sleep(5)
# raw_input('Wait to open and then enter')
print('Got input...moving on')
b.execute_script('window.scrollTo(0,8000)')
start = 10000
# b.set_page_load_timeout(100)
for i in range(30):
    try:
        start += random.randrange(6000, 8000)
        b.execute_script('window.scrollTo(0,%d)' % start)
        sleep(5)
    except:
        i -= 1
#    time.sleep(3)
    print('Iteration %d' % i)
print('Loop completed')
# sleep(30)
s = b.page_source
s = s.encode('utf-8')
print('Got source code')
with open('abstract_wallpaper.txt', 'wb') as f:
    f.write(s)
print('Done!!')
