# This file is for extracting online and valid phish from PhishTank

import csv
import time
from bs4 import BeautifulSoup
from common import utils

def getIds(no: int = 20, phish: bool = True, online: bool = True) -> list():
    ids = list()

    for i in range(0, int(no/20)):
        p = "y" if phish else "n"
        if phish and online:
            o = "y"
        elif not phish and online:
            o = "All"
        else:
            o = "n"

        requestUrl = "https://www.phishtank.com/phish_search.php?page="+str(i)+"&active="+o+"&valid="+p+"&Search=Search"
        source = utils.getHttpResponse(requestUrl)
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find("table", {"class": "data"})
        
        for row in table.find_all("tr", {"style": "background: #ffffcc;"}):
            cell = row.find("td")
            anchorText = cell.find("a").get_text()
            ids.append(anchorText)

        #time.sleep(10)
        print('- Fetching Page'+str(i))

    return ids

def getUrl(id: str):
    requestUrl = "https://www.phishtank.com/phish_detail.php?phish_id=" + id
    source = utils.getHttpResponse(requestUrl)
    soup = BeautifulSoup(source, 'html.parser')
    divUrl = soup.find("div", {"class": "url"}) # not this div but the next one
    divWeWant = divUrl.find_next("div") # this div contains the span and the b
    span = divWeWant.find("span")
    b = span.find("b")
    return b.get_text()



userinput = 0
while userinput!='4':
    print('Enter your choice:')
    print('1. Fetch IDs')
    print('2. Fetch Phish URLs')
    print('3. Fetch Good URLs')
    print('4. Quit')
    userinput = input('Enter: ')
    if userinput=='1':
        with open('dataset/goodIds.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Header
            writer.writerow(['id'])
            goodIds = getIds(500, False)
            for i in goodIds:
                writer.writerow([i])
        with open('dataset/phishIds.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Header
            writer.writerow(['id'])
            phishIds = getIds(500, True)
            for i in phishIds:
                writer.writerow([i])

    if userinput=='2':
        # Read IDs
        phishIds = []
        with open('dataset/phishIds.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                phishIds.append(i['id'])
        # Get URL
        with open('dataset/urls.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Header
            #writer.writerow(['url', 'result'])
            countPhish = 0
            for i in phishIds:
                url = getUrl(i)
                writer.writerow([url, 1])
                if countPhish%10==0:
                    print('- Fetching Phishing URL #'+str(countPhish))
                if countPhish%50==0:
                    print('- Pausing 10 seconds.')
                    time.sleep(10)
                    print('- Resumed')
                countPhish+=1

    if userinput=='3':
        # Read IDs
        goodIds = []
        with open('dataset/goodIds.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i in reader:
                goodIds.append(i['id'])
        # Get URL
        with open('dataset/urls.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Header
            #writer.writerow(['url', 'result'])
            countGood = 0
            for i in goodIds:
                url = getUrl(i)
                writer.writerow([url, 0])
                if countGood%10==0:
                    print('- Fetching Good URL #'+str(countGood))
                if countGood%50==0:
                    print('- Pausing 10 seconds.')
                    time.sleep(10)
                    print('- Resumed')
                countGood+=1