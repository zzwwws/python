#统计网易一元夺宝中奖者投注金额分布情况，如#iPhone6 Plus 5.5英寸 16G，截至2015-03-26一共1543期，投注10元中奖的次数最高，380次，其次是投注2元次数是300次。这个统计并不能证明投2元划算，需要考虑每一期投2元的人数和投10元的人数，仅供参考。
#-*- coding: utf-8 -*-
import urllib2
import mechanize
import random
import matplotlib.pyplot as pyplot
import matplotlib
from bs4 import BeautifulSoup
import re

#iPhone6 4.7英寸 64G
ROOT_URL = 'http://1.163.com/m/history/01-48-00-'
#iPhone6 Plus 5.5英寸 64G
ROOT_URL = 'http://1.163.com/m/history/01-77-00-'
#iPhone6 Plus 5.5英寸 16G
#ROOT_URL = 'http://1.163.com/m/history/01-37-00-'

#伪装成浏览器，暂时注释
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

page_str = str('')
tmp = ['0','0','0','0']

#生成页码 如1948 -->‘19-48’ 
def formatPage(page):
    for d in range(4):
        tmp[d] = str(page % 10)
        page /= 10
	page_str = tmp[-1] + tmp[-2] + '-'+tmp[1]+tmp[0]
    return page_str
	
#从content中匹配关键词regex
def extractData(regex, content, index=1):  
    r = '0'  
    p = re.compile(regex)  
    m = p.search(content)  
    if m:  
        r = m.group(index)  
    return r  
  
regex = r'用户ID：(.*) '
#regex = r'本期参与：(.*)人次'
dest_url = str('')
hist={}
for i in range(1,1543):
	print formatPage(i)
	dest_url = ROOT_URL + formatPage(i) + '.html'
	response = urllib2.urlopen(dest_url)
	key_num = extractData(regex, response.read())
	print key_num
	hist[key_num] = hist.get(key_num,0)+1;

#画图
font = matplotlib.font_manager.FontProperties(fname='c:\\windows\\fonts\\simsun.ttc')
hist_sorted = sorted(hist.iteritems(), key=lambda d: d[1], reverse=True)
print hist_sorted
bar_width = 0.35
pyplot.bar(range(20), [hist_sorted[i][1] for i in range(20)],bar_width)
pyplot.xticks(range(20), [hist_sorted[i][0] for i in range(20)], fontproperties=font,rotation=30)
pyplot.show()
	
