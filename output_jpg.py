#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

# http://pythontutorial.net/python-basics/python-write/csv-file

def getdata(url):
    r = requests.get(url)
    return r.text

# page 1
htmldata = getdata("http://bindfix.net/site/temp_site/body_page.html")
soup = BeautifulSoup(htmldata, 'html.parser')

# page 2
htmldata = getdata("http://bindfix.net/site/temp_site/frame_1.html")
frame_1 = BeautifulSoup(htmldata, 'html.parser')

page_title = soup.title

page_body = soup.title

# print the result
print(page_title, page_body)
