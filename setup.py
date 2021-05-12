from os import link, name
from sys import winver
from bs4 import BeautifulSoup
import requests
import csv
import urllib3
import re
link = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://downtowndallas.com/experience/stay/'
sv = requests.get(url,headers=headers)
clean = re.compile('<.*?>')
space = re.compile(r'\s+')
reg = re.compile("\d{3}\d{3}\d{4}")
if sv.status_code==200:
    soup=BeautifulSoup(sv.content, 'lxml')
    resultpage = soup.find_all('a',class_='place-square__btn')
    for result in resultpage:
        l = re.findall("href=[\"\'](.*?)[\"\']", str(result))
        link.append(l[0])
        
for li in link:
    
    sv = requests.get(li,headers=headers)

    if sv.status_code==200:
        soup=BeautifulSoup(sv.content, 'lxml')
        placename = str(soup.find('h1',class_='place-name'))        
        placename = (placename[23:-5])
        placeadd = str(soup.find('div',class_='place-info-address'))
        placeadd = str(re.sub(clean,'',placeadd))
        placeadd = re.sub(space,"",placeadd)
        print(placeadd)

        placeno = (re.findall("\d{3}-\d{3}-\d{4}",str(soup)))
        if len(placeno)>0:
            placeno = placeno[0]
        print(placeno)

        placearea = str(soup.find_all('div',class_='place-info-address'))
        placearea = (re.sub(clean,'',placearea))
        placearea = re.sub(space,"",placearea)
        placearea = placearea.split(',')
        placearea = str(placearea[-1])[:-1]
        print(placearea)
        

        img = str(soup.find('img', class_='attachment-hero size-hero'))
        img = re.findall("src=[\"\'](.*?)[\"\']", str(img))
        print(img)
        data = [placename, placeadd, placeno, placearea,str(img[0])]

        with open('data.csv', 'a', newline='',encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerow(data)

