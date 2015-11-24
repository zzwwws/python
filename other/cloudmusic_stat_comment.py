#encoding: UTF-8
import locale  
import requests  
import json  
import sys  

		
header = {
    'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'music.163.com',
	'Referer':'http://music.163.com/song?id=27678655',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    }
	
def get_comment_str():
	
	response = requests.get("http://music.163.com/api/v1/resource/comments/R_SO_4_27678655/?rid=R_SO_4_27678655&offset=0&total=true&limit=20&csrf_token=",headers=header) 

	comment_json = json.loads(response.text)

	code = comment_json.get('code')
	if(code == 200):	
		comments = comment_json.get('comments')
		return [comment.get('content') for comment in comments]
	else:
		return[]
content = ''
for ct in get_comment_str():
	if isinstance(ct,unicode):
		content += ct
print content