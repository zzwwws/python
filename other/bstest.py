#-*- coding: utf-8 -*-
import urllib2
import mechanize
import random
import matplotlib.pyplot as pyplot
import matplotlib
from bs4 import BeautifulSoup
import re

ROOT_URL = 'http://1.163.com/m/history/01-48-00-00-01.html'

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = urllib2.urlopen(ROOT_URL);

page_str = str('')
tmp = []
def formatPage(page):
    for d in range(4):
        print d
        tmp[d] = page % 10
        page /= 10
    page_str = d[-1]+d[-2]+'-'+d[1]+d[0]
    print page_str
    
def extractData(regex, content, index=1):  
    r = '0'  
    p = re.compile(regex)  
    m = p.search(content)  
    if m:  
        r = m.group(index)  
    return r  
  
regex = r'与：(.*)人次'

for i in range(1,1949):
    formatPage(i)

