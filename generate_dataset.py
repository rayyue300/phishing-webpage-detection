# This file is for generating dataset from the fetched urls

import csv
import threading
from features_extraction import code
from features_extraction import url_and_domain

def generate():
    count = 0
    with open('dataset/urls.csv', newline='') as urlfile:
        urlrows = csv.DictReader(urlfile)
        
        # Header
        with open('dataset/dataset.csv', 'w', newline='') as dsfile:
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
                "RESULT"
            ])

        for urlrow in urlrows:
            url = urlrow['url']
            result = urlrow['result']

            results = list()

            try:
                threads = []

                # URL and Domain based
                uFeatures = [None] * 5
                def jobUD(url: str):
                    uFeatures[0] = url_and_domain.isDomainHavingNonAscii(url)
                    uFeatures[1] = url_and_domain.isShortUrl(url)
                    uFeatures[2] = url_and_domain.isDeepLevelSubdomain(url)
                    uFeatures[3] = url_and_domain.isLowAlexaRank(url)
                    uFeatures[4] = url_and_domain.isNotIndexedByGoogle(url)
                threads.append(threading.Thread(target=jobUD, args=[url]))

                # Code based
                cFeatures = [None] * 5
                def jobCs(no: int, url: str):
                    switcher = {
                        0: code.isRedirectingToOtherDomain(url),
                        1: code.isUsingManyExternalResources(url),
                        2: code.isOpenningNewWindow(url),
                        3: code.isBlockingRightClick(url),
                        4: code.isUsingInceptionBar(url)
                    }
                    cFeatures[no] = switcher.get(no)
                
                for i in range(0,5):
                    threads.append(threading.Thread(target=jobCs, args=[i, url]))

                for t in threads:
                    t.start()

                for t in threads:
                    t.join()

                for u in uFeatures:
                    results.append(u)
                for c in cFeatures:
                    results.append(c)

                count += 1
            except:
                pass

            # This append the result extracted from Phishtank
            results.append(result)

            # Save
            with open('dataset/dataset.csv', 'a', newline='') as dsfile:
                writer = csv.writer(dsfile)
                writer.writerow(results)
            
            print("Extracted: "+str(count))

generate()