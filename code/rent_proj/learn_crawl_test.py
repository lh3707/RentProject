#-*- coding:utf-8 -*-

import requests

resp = requests.get('https://www.baidu.com')
print(resp)
print(resp.content)