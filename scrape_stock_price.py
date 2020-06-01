# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:36:34 2020

@author: HinePo
"""

import bs4
import requests
import time


def get_price():
    
    # get URL
    r = requests.get('https://finance.yahoo.com/quote/GC=F?p=GC=F')
    
    # create soup element / parse the html
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    
    # scrape price: inspect element from website
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    
    return price

# Loop and print every x seconds
x = 5
while True:
    print('Current price: ' + str(get_price())) 
    time.sleep(x)