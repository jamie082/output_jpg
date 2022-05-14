#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import csv

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

filename = "output_file.csv"

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile)

    # write the header
    writer.writerow(all_imgs)

    # write the column
    writer.writerow(classes_select)
