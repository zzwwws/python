#统计一元夺宝土豪们的投注偏好
#-*- coding: utf-8 -*-
import urllib2
import matplotlib.pyplot as pyplot
import matplotlib
import json

#尼玛这个人花了1000w在上面，怀疑是不是npc
CID = '13578716'
#这个人也花了500w
#CID = '19135221'


def get_history_list(url):
	
	response = urllib2.urlopen(url)
	js = json.loads(response.read())

	dump_js = json.dumps(js,ensure_ascii=False)

	#json like this
	'''
    "code": 0,
    "result": {
        "status": 9,
        "pageNum": 9,
        "pageSize": 10,
        "list": [
            {
                "status": 3,
                "goods": {
                    "typeId": 1,
                    "regularBuyMax": 50,
                    "wishSetable": 0,
                    "priceBase": 0,
                    "price": 9800,
                    "priceUnit": 1,
                    "buyable": true,
                    "tag": null,
                    "brand": 1,
                    "gpic": 
	'''
	#result is type of dict
	result = js.get('result')

	list = result.get('list')
	return list
page_size = 1
ROOT_URL = 'http://1.163.com/m/user/duobaoRecord/get.do?cid=%s'%(CID)
sum = 0
dict_product={}
dict_time={}
dict_date={}
dict_cost={}

def init_time_dict():
	for n in range(0,24):
		key = str(n)
		value = 0
		dict_time[key] = value
		
#解析时间格式如2015-03-19 10:53:00.000到dict_time中
def parse_time(time_str):
	#切片到hour
	key = time_str[11:13]
	return key


def plot(dict_s,title):
	font = matplotlib.font_manager.FontProperties(fname='c:\\windows\\fonts\\simsun.ttc')

	list_sorted = sorted(dict_s.iteritems(), key=lambda d: d[1], reverse=True)
	bar_width = 0.35
	pyplot.bar(range(20), [list_sorted[i][1] for i in range(20)],bar_width)
	pyplot.xticks(range(20), [list_sorted[i][0] for i in range(20)], fontproperties=font,rotation=30)
	pyplot.title(title ,fontproperties=font)
	pyplot.show()
	
#初始化时间dict

init_time_dict()
while True:
	dest_url = ROOT_URL +'&pageSize='+str(page_size)+'&pageNum=10&status=9'
	print dest_url
	list = get_history_list(dest_url)
	if(len(list) == 0):
		break
	page_size += 1
	for content in list:
		price = content.get('goods').get('price')
		gname = content.get('goods').get('gname')
		time = content.get('calcTime')
		dict_product[gname] = dict_product.get(gname,0) + 1
		if (time != None):
			time_in_hour = parse_time(time)
			dict_time[time_in_hour] = dict_time.get(time_in_hour,0) + 1
		num = content.get('num')
		dict_cost[gname] = dict_product.get(gname,0) + num
		sum += num
print sum

#土豪最喜欢投注那个产品
plot(dict_product,u'土豪最喜欢的产品前20')

#土豪最喜欢在什么时候投注
plot(dict_time,u'土豪最喜欢投注时间前20')

#土豪在什么产品上花的钱最多
plot(dict_cost,u'土豪在什么产品上花的钱最多')

	


	
