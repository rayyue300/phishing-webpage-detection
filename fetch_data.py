# This file is for extracting online and valid phish from PhishTank

import csv
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

def saveUrls():
    phishIds = getIds(1000, True)
    goodIds = getIds(1000, False)

    with open('dataset/urls.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Header
        writer.writerow(['url', 'result'])

        #Phish
        countPhish = 0
        for i in phishIds:
            if countPhish%10==0:
                print('Fetching Phishing URL #'+str(countPhish))
            url = getUrl(i)
            writer.writerow([url, 1])
            countPhish+=1

        #Safe
        countGood = 0
        for i in goodIds:
            if countGood%10==0:
                print('Fetching Good URL #'+str(countGood))
            url = getUrl(i)
            writer.writerow([url, 0])
            countGood+=1


#print("ID: 6347670")
#print(getUrl("6347670"))
saveUrls()