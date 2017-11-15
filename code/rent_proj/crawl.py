# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import csv,codecs
from urllib.parse import urljoin

url = "http://xa.58.com/yanta/pinpaigongyu/pn/{page}/?minprice=1000_1500"

# page number ,init 0
page = 0

csv_file = open("rent.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
	page += 1
	print("fetch: ", url.format(page=page))
	response = requests.get(url.format(page=page))
	html = BeautifulSoup(response.text, 'lxml')
	house_list = html.select(".list > li")
	house_next = html.select(".next")

	if not house_next:
		break

	for house in house_list:
		house_title = house.select("h2")[0].string
		house_url = urljoin(url, house.select("a")[0]["href"])
		house_info_list = house_title.split()

		house_location = house_info_list[1]

		# if gongyu in house_info_list[1] or qingnianshequ in \
		# house_info_list[1]:
		# 	house_location = house_info_list[0]
		# else:
		# 	house_location = house_info_list[1]

		house_money = house.select(".money")[0].select("b")[0].string
		csv_writer.writerow([house_title, house_location, house_money, house_url])

csv_file.close()











# with open('csv_file','wb') as f:
# 	f.write(csv_file, delimiter=',') 

