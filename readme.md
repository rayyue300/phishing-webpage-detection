# Phishing Webpage Detection
[![Build Status](https://travis-ci.org/rayyue300/phishing-webpage-detection.svg?branch=master)](https://travis-ci.org/rayyue300/phishing-webpage-detection)

This project makes use of machine learning to detect phishing webpage.
Working in progress, early stage.

## Environment
### Development
1. Python 3.6
1. Visual Studio Code
1. Mac OS Catalina

## Milestones
### Functions for Features Extraction
#### URL and Domain based
1. Does the domain contain non-ASCII characters?
1. Does the URL using an URL shortening service?
1. Does the URL have deep level of subdomain?
1. Does the URL have low Alexa rank?
1. Is the domain not indexed by Google?

#### Code based
1. Is the URL redirecting to other domain?
1. Does the URL use many external resources?
1. Does the URL open new windows?
1. Does the URL block right clicks?
1. Does the URL use inception bar? ([Ref](https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/))

#### Content based (Future)


### Generate Small Data Set
#### Fetch URLs from PhishTank
A script is written to fetch phish URLs and non-phish URLs.
To execute it, go to the project root directory and execute
```bash
python3 fetch_data.py
```

By default, it fetch 100 phish URLs and 100 non-phish URLs.
This can be modified in the saveUrls() function.

#### Extract Features and Generate Dataset
> *Better execute in virtual machine* because it opens those phishing webpages.
Another script is written to do the features extraction and generate the CSV file.
To execute it, go to the project root directory and execute
```bash
python3 generate_dataset.py
```

### Simple Machine Learning (In Progress)
At the current stage, the following algorithms are used for machine learning.
* Logistic Regression
* Decision Tree
* Random Forest
```bash
python3 machine_learn.py
```

## Unit Tests
Unit tests are written to test specific modules / functions.
To execute tests, go to the project root directory and execute
```bash
python3 -m unittest
```