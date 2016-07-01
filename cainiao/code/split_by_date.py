#-*-coding:utf-8-*-
'''
将文件存成csv文件
将item_feature.csv按照日期分割成不同的文件
'''

import csv
import os
import cPickle

date_dictionary = {}

def writeByDate(date,words):
	file_name = date + ".csv"
	os.chdir('../data4/all/date/')
	if date not in date_dictionary:
		date_dictionary[date] = True
		with open(file_name,'a') as f:
			write = csv.writer(f)
			write.writerow(["date","item_id","cate_id","cate_level_id","brand_id","supplier_id","pv_ipv","pv_uv","cart_ipv","cart_uv","collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay","ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs","amt_alipay_njhs","qty_alipay_njhs","unum_alipay_njhs"])
			write.writerow(words)
	else:
		with open(file_name,'a') as f:
			write = csv.writer(f)
			write.writerow(words)
	os.chdir('../../../code')

def splitByDate():
	with open("../data4/item_feature2.csv") as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			date = row[0]
			words = [row[0][:4]+"-"+row[0][4:6]+'-'+row[0][6:]] + row[1:]
			writeByDate(date,words)

splitByDate()

def savepkl():
	dict = {}
	with open("../data4/item_feature2.csv") as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			date = row[0][:4]+"-"+row[0][4:6]+'-'+row[0][6:]
			item_id = row[1]
			store_code = row[2]
			dict[(date,item_id,store_code)] = row[2:]

	with open("../data4/item_feature2.pkl",'wb') as f:
		cPickle.dump(dict,f,-1)
# savepkl()
