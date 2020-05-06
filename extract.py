# This file is for extracting features from a given URL

import threading, time

from features_extraction import code
from features_extraction import url_and_domain
from features_extraction import keyword

url = input('Enter the URL for feature extraction: ')

# Initialize
progress = 0            # store current no. of finished thread
maxProgress = 15        # store total no. of threads to be executed
startTime = time.time() # store current time
threads = []            # store all the threads to be executed

# Decalre variables to store features value
uFeatures = [None] * 5
cFeatures = [None] * 5
kFeatures = [None] * 5
results = list()        # store the result of all features

# Create jobs for URL based features
def jobUs(no: int, url: str):
    global progress
    switcher = {
        0: url_and_domain.isDomainHavingNonAscii(url),
        1: url_and_domain.isShortUrl(url),
        2: url_and_domain.isDeepLevelSubdomain(url),
        3: url_and_domain.isLowAlexaRank(url),
        4: url_and_domain.isNotIndexedByGoogle(url)
    }
    uFeatures[no] = switcher.get(no)
    progress+=1

# Create jobs for Code based features
def jobCs(no: int, url: str):
    global progress
    switcher = {
        0: code.isRedirectingToOtherDomain(url),
        1: code.isUsingManyExternalResources(url),
        2: code.isOpenningNewWindow(url),
        3: code.isBlockingRightClick(url),
        4: code.isUsingInceptionBar(url)
    }
    cFeatures[no] = switcher.get(no)
    progress+=1

# Create jobs for Keyword based features
def jobKs(no: int, url: str):
    global progress
    switcher = {
        0: keyword.isPageContainingLogin(url),
        1: keyword.isPageContainingCreditCard(url),
        2: keyword.isPageContainingDownload(url),
        3: keyword.isPageContainingUrgent(url),
        4: keyword.isPageContainingActionRequired(url)
    }
    kFeatures[no] = switcher.get(no)
    progress+=1

# Create job for showing progress
def showProgress():
    global progress
    prevProgress = 0
    while progress<maxProgress:
        elapsedTime = time.time()-startTime
        print('Elapsed Time: '+str(elapsedTime))
        if progress!=prevProgress:
            prevProgress = progress
            print('Extracted Features: '+str(progress)+'/'+str(maxProgress))
            #print(str(progress/maxProgress*100)+'%')
        time.sleep(5)

# Add threads into the thread pool
threads.append(threading.Thread(target=showProgress))
for i in range(0,5):
    threads.append(threading.Thread(target=jobUs, args=[i, url]))
    threads.append(threading.Thread(target=jobCs, args=[i, url]))
    threads.append(threading.Thread(target=jobKs, args=[i, url]))

# Start all threads
for thread in threads:
    thread.start()

# Join all threads
for thread in threads:
    thread.join()

# Store the results
for u in uFeatures:
    results.append(u)
for c in cFeatures:
    results.append(c)
for k in kFeatures:
    results.append(k)

print("Completed. Result:")
print(results)