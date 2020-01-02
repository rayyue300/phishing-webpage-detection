# Phishing Webpage Detection
[![Build Status](https://travis-ci.org/rayyue300/phishing-webpage-detection.svg?branch=master)](https://travis-ci.org/rayyue300/phishing-webpage-detection)

This project makes use of machine learning to detect phishing webpage.
Working in progress, early stage.

## Environment
1. Python 3.6
1. Visual Studio Code
1. Mac OS Mojave

## Milestones
### Functions for Features Extraction
#### URL and Domain based
1. Does the domain contain non-ASCII characters?
1. Does the URL using an URL shortening service?
1. Does the URL have deep level of subdomain?
1. Does the URL have low Alexa rank?
1. Is the domain not indexed by Google?

#### Code based (In Progress)
1. Does the URL have many redirections?
1. Does the URL use many external resources?
1. Does the URL open new windows?
1. Does the URL block right clicks?
1. Does the URL use inception bar? [Ref](https://jameshfisher.com/2019/04/27/the-inception-bar-a-new-phishing-method/)

#### Content based


### Generate Data Set

### Machine Learning

## Unit Tests
Unit tests are written to test specific modules / functions.
To execute tests, go to the project root directory and execute
```bash
python3 -m unittest
```