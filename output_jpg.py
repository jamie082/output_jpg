#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import openpyxl

xlsx = openpyxl.Workbook()
sheet = xlsx.active

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

all_imgs = soup.find_all('img')

classes_select = frame_1.find(class_="Windows").get_text()

for image in all_imgs:
    print(image['src'])


sheet['A1'] = all_imgs
sheet['B1'] = classes_select


xlsx.save('sample.xlsx')
