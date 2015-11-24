import urllib;
import urllib2;

cmb_url = "http://mlife.cmbchina.com/NeptuneApp/createOrderV2.json"

values = {}
values['_pro'] = '0'
values['_pla'] = 'pluto_andr_4.1.0_uni_cmbccd'
values['_ver'] = '4.1.0'
values['_mt'] = 'GOOGLE,OCCAM,4.4.4'
values['appId'] = '744f2f53e778446381e410ac3844259a'
values['_appId'] = '744f2f53e778446381e410ac3844259a'
values['DeviceId']='357541051314179'
values['_r'] = 'no'
values['_channel']='cmbccd'
values['_uid']='5a3f0435fdb91eb506eddbfa7884d125'
values['payType']='1'
values['mac'] = 'bcda561caeee682d60c2dde4df50577a'
values['quantity']='1'
values['accountId']='5a3f0435fdb91eb506eddbfa7884d125'
values['productId']='0060000000948'
values['orderPoint']='9'

data = urllib.urlencode(values)
req = urllib2.Request(cmb_url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page