__author__ = 'zzwwws'
#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
import json

STOCK_CODE_URL = 'http://quote.eastmoney.com/stocklist.html'
STOCK_INFO_URL = 'http://quotes.money.163.com/app/stock/#.json'
STOCK_INFO_MORE_URL = 'http://api.money.126.net/data/feed/#,MARKET_HS'

def sh_or_sz(href):
    return href and re.compile("http://quote.eastmoney.com/[sh,sz]").search(href)

def query_stock(code):
    if code.startswith('00'):
        codep = '1' + code
    elif code.startswith('60'):
        codep = '0' + code
    elif code.startswith('30'):
        codep = '1' + code
    tuple_1 = query_stock_info(codep)
    tuple_2 = query_stock_info_cur(codep)

    if tuple_1[0] is None or tuple_2[1] is None or tuple_1[0] == 0:
        pe = '--'
    else:
        pe = (tuple_2[1] * 1.0)/(tuple_1[0]*1.0)

    if tuple_2[1] is None or tuple_1[1] is None or tuple_1[1] == 0:
        ra = '--'
    else:
        ra = (tuple_2[1]*1.0)/(tuple_1[1]*1.0)
    return code, tuple_2[2], tuple_1[1], tuple_1[2], tuple_2[1], ra, tuple_2[0], pe

def query_stock_info(code):
    urlstr = urllib2.urlopen(STOCK_INFO_URL.replace('#', code))
    js = json.load(urlstr).get('data')
    return js[0].get('MFSUM'), js[0].get('WEEK52_HIGH'), js[0].get('WEEK52_LOW')

def query_stock_info_cur(code):
    urlstr = urllib2.urlopen(STOCK_INFO_MORE_URL.replace('#', code)).read()
    jsonstr = urlstr[urlstr.find('(')+1:urlstr.rfind(')')]
    js = eval(jsonstr).get(code)
    return js.get('percent'), js.get('price'), js.get('name'), js.get('yestclose')

def format_stock_item(stock_item):
    line = str('')
    for item in stock_item:
        if item is None:
            line += '--' + '\t'
        else:
            line += str(item) + '\t'
    line += '\n'
    return line

response = urllib2.urlopen(STOCK_CODE_URL)
soup = BeautifulSoup(response, 'html.parser')
file_handle = open('stock_info.reduced', 'w')
for link in soup.find_all(href=sh_or_sz):
    i = 1
    link_text = link.get_text()
    if link_text.find('(') != -1:
        stock_code = link_text[link_text.find('(')+1:-1]
        if stock_code.startswith('60') or stock_code.startswith('30') or stock_code.startswith('00'):
            try:
                stock_tuple = query_stock(stock_code)
            except Exception, e:
                continue
            file_handle.write(format_stock_item(stock_tuple))
            print('finish   ' + stock_code)
            i += 1
file_handle.close()




