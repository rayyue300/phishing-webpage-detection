import sys, getopt, time, threading, joblib
import numpy as np

from features_extraction import code
from features_extraction import url_and_domain
from features_extraction import keyword

progress = 0            # store current no. of finished thread
maxProgress = 15        # store total no. of threads to be executed
startTime = time.time() # store current time
threads = []            # store all the threads to be executed
uFeatures = [None] * 5
cFeatures = [None] * 5
kFeatures = [None] * 5
results = list()        # store the result of all features

def main(argv):
    # Get URL from command line arguments
    url = ''
    try:
        opts, args = getopt.getopt(argv,"hu:")
    except getopt.GetoptError:
        print('predict.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('predict.py -u <url>')
            sys.exit()
        elif opt in ("-u"):
            url = arg

    # Extract features
    print('Extracting features from '+url)
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
            print('- Elapsed Time: '+str(round(elapsedTime))+'s\t('+str(progress)+'/'+str(maxProgress)+')')
            time.sleep(10)

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
    
    print('- Elapsed Time: '+str(round(time.time()-startTime))+'s\tDone')
    print('- '+str(results))

    # Prediction
    print('Predicting')
    classifier = joblib.load('final_models/decision_tree.pkl')
    predictStart = time.time()
    #results2D = np.reshape(results, (1, -1))
    results2D = np.array(results).reshape((1, -1))
    prediction = classifier.predict(results2D)
    elapsedTime = time.time()-predictStart
    print('- Elapsed Time: '+str(round(time.time()-predictStart))+'s\tDone')
    result = int(prediction[0])
    if result==0:
        print('- NOT PHISHING')
    elif result==1:
        print('- PHISHING')
    else:
        print('- ERROR')

if __name__ == "__main__":
   main(sys.argv[1:])