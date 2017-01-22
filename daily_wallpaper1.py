from bs4 import BeautifulSoup as bs
import re
import urllib
import random
import shutil
import requests
import os
import MySQLdb


def download_and_set_wallpaper(url):
    filename = re.findall('.+\/(.+)', url)[0]
    if filename not in os.listdir(os.getcwd()):
	    print('Downloading your wallpaper....')
	    response = requests.get(url, stream=True)
	    with open(filename, 'wb') as out_file:
	        shutil.copyfileobj(response.raw, out_file)
	    del response
	os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/vbshah/python/%s' % filename)
#    print('/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/vbshah/python/%s' % filename)

def mysql_connect(host, usrname, password, dbname):
	try:
		db = MySQLdb.connect(host, usrname, password, dbname)
		return db.cursor()
	except:
		return None
with open('abstract_wallpaper.txt') as f:
    filedata = f.read()
soup = bs(filedata, 'lxml')
images = soup('img')
links = []
for j, i in enumerate(images):
    i = str(i.get('src'))
    tmp_link = re.findall('(h.+)\?h', i)
    if len(tmp_link):
        links.append(tmp_link[0])
        # print(tmp_link[0])
        # print('filename', )
# print(len(links))
# old result : 60
# new result : 201 !
random_link = random.choice(links)
download_and_set_wallpaper(random_link)
print('Done!')
# print("And the random link is %s" % random_link)
