# This file is for generating dataset from the fetched urls
# Version 2

import threading, csv, os.path, time, math

from features_extraction import code
from features_extraction import url_and_domain
from features_extraction import keyword

datasetFile = 'dataset/dataset.csv'
urlsFile = 'dataset/urls.csv'
progress = 0                        # number of URLs done feature extraction
startTime = time.time()             # store current time

# Create file if not exist
if not os.path.exists(datasetFile):
    with open(datasetFile, 'w', newline='') as dsfile:
        writer = csv.writer(dsfile)
        writer.writerow([
            "NonAsciiDomain",
            "ShortURL",
            "DeepSubdomain",
            "LowAlexa",
            "NoGoogleIndex",
            "RedirectAway",
            "ExternalRes",
            "NewWindow",
            "BlockRClick",
            "InceptionBar",
            "Login",
            "CreditCard",
            "Download",
            "Urgent",
            "ActionRequired"
            "RESULT"
        ])

# Read URLs and results from the file
with open(urlsFile, newline='') as urlfile:
    urlrows = list(csv.DictReader(urlfile))

# Create job to generate one row
def jobOneRow(url: str, result: str):
    global progress
    results = list()
    uFeatures = [None]*5
    cFeatures = [None]*5
    kFeatures = [None]*5
    threads = []
    # Create jobs for URL based features
    def jobUs(no: int, url: str):
        switcher = {
            0: url_and_domain.isDomainHavingNonAscii(url),
            1: url_and_domain.isShortUrl(url),
            2: url_and_domain.isDeepLevelSubdomain(url),
            3: url_and_domain.isLowAlexaRank(url),
            4: url_and_domain.isNotIndexedByGoogle(url)
        }
        uFeatures[no] = switcher.get(no)
    # Create jobs for Code based features
    def jobCs(no: int, url: str):
        switcher = {
            0: code.isRedirectingToOtherDomain(url),
            1: code.isUsingManyExternalResources(url),
            2: code.isOpenningNewWindow(url),
            3: code.isBlockingRightClick(url),
            4: code.isUsingInceptionBar(url)
        }
        cFeatures[no] = switcher.get(no)
    # Create jobs for Keyword based features
    def jobKs(no: int, url: str):
        switcher = {
            0: keyword.isPageContainingLogin(url),
            1: keyword.isPageContainingCreditCard(url),
            2: keyword.isPageContainingDownload(url),
            3: keyword.isPageContainingUrgent(url),
            4: keyword.isPageContainingActionRequired(url)
        }
        kFeatures[no] = switcher.get(no)
    # Add threads into the thread pool
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
    # This append the result extracted from Phishtank
    results.append(result)
    # Save
    with open(datasetFile, 'a', newline='') as dsfile:
        writer = csv.writer(dsfile)
        writer.writerow(results)
    progress+=1
    print('Progress:\t'+str(progress)+'/'+str(len(urlrows)))
    print('Elapsed time: \t'+str(round(time.time()-startTime)))



for i in range(0, math.ceil(len(urlrows)/2), 2):
#for i in range(0, 15, 5):
    threads = []
    for j in range(0, 2):
        threads.append(threading.Thread(target=jobOneRow, args=[urlrows[i+j]['url'],urlrows[i+j]['result']]))
    for t in threads:
        t.start()
    for t in threads:
        t.join()