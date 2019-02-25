
import os
import os.path
import io
import sys
import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import string

stranger_user = input("Enter a stranger's Twitter username: ")
your_user = input("Enter your username: ")

#check for existence in mock database / time period

#launch into the project
os.system("python3 /home/jess/Projects/cardsforhumanity/02scraping.py " + stranger_user)
os.system("python3 /home/jess/Projects/cardsforhumanity/02scraping.py " + your_user)


