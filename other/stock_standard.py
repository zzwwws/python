__author__ = 'zzwwws'
#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re

STOCK_CODE_URL = 'http://quote.eastmoney.com/stocklist.html'
ROOT_URL = 'http://ichart.yahoo.com/table.csv?s=#'

def sh_or_sz(href):
    return href and re.compile("http://quote.eastmoney.com/[sh,sz]").search(href)

def format_code(code):
    if code.startswith('60'):
        codep = code + ".SS"
    else:
        codep = code + ".SZ"
    return codep

def write_table_to_file(code):
    fp = urllib2.urlopen(ROOT_URL.replace('#',format_code(code)), timeout = 20)
    with open("E:/table1/table_" + code + ".csv", "wb") as code:code.write(fp.read())

response = urllib2.urlopen(STOCK_CODE_URL)
soup = BeautifulSoup(response, 'html.parser')
file_handle = open('stock_info.reduced', 'w')
for link in soup.find_all(href=sh_or_sz):
    i = 1
    link_text = link.get_text()
    if link_text.find('(') != -1:
        stock_code = link_text[link_text.find('(')+1:-1]
        if stock_code.startswith('30'):
            try:
                write_table_to_file(stock_code)
            except Exception, e:
                print(e.message)
                continue
            print('finish   ' + stock_code)
            i += 1
file_handle.close()

