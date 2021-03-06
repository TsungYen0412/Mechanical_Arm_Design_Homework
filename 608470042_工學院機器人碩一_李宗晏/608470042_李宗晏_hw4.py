#! /usr/bin/env python3

#-*-coding:UTF-8 -*-
# 範例程式 EX02_07.py
#
# 下面 zipcode 存放台北市，基隆市，新北市各區的郵遞區號
#
# Q1.如何透過迴圈把台北市的所有郵遞區號列出 
# Q2.如何輸入一個區域名稱，找出這個區域所代表的郵遞區號?  (ex. 輸入:信義區  回傳:201)
# Q3.如何輸入一個郵遞區號後，找出這個郵遞區號所代表的區域? (ex. 輸入:106  回傳:大安區)

zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105, "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112, "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202, "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}


def list_zip(city):
	#print(city, "內所有區域的郵遞區號: ", list(zipcode[city].values()),sep='')＃這執行速度快多了
	print(city, "內所有區域的郵遞區號: ", sep='', end='')
	for i in list(zipcode[city].values()):#題目說要用迴圈
		if list(zipcode[city].values()).index(i) is not (len(list(zipcode[city].values()))-1):
			print(i, ", ", sep='',end='')
		else:
			print(i)


def area_to_zip(area):
	city = []
	postal_code = []
	for i in list(zipcode.keys()):
		if area in list(zipcode[i].keys()):
			city.append(i)
			postal_code.append(zipcode[i][area])
	return city, postal_code


def zip_to_area(postal_code):
	for i in list(zipcode.keys()):
		if postal_code in list(zipcode[i].values()):#為了提高執行速度
			for j in list(zipcode[i].keys()):
				if zipcode[i][j] == postal_code:
					return j


if __name__ == '__main__':
	print("******************************  Q1  ******************************")
	city = input("輸入城市名稱(ex. 台北市): ")
	list_zip(city)

	print("******************************  Q2  ******************************")
	area = input("輸入區域名稱(ex. 信義區): ")
	city, postal_code = area_to_zip(area)
	for i in range(len(city)):
		print("(\'", city[i], "\',", postal_code[i], ")", sep='')

	print("******************************  Q3  ******************************")
	postal_code = int(input("輸入郵遞區號(ex. 106): "))
	area = zip_to_area(postal_code)
	print(area)

