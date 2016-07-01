#-*-coding:utf-8-*-
'''
将文件存成csv文件
将item_feature.csv按照item分割成不同的文件
'''

import csv
import os
import cPickle

item_dictionary = {}

def writeByItem(item_id,words):
	file_name = item_id + ".csv"
	os.chdir('../data4/store/store/5/')
	if item_id not in item_dictionary:
		item_dictionary[item_id] = True
		with open(file_name,'a') as f:
			write = csv.writer(f)
			write.writerow(["date","item_id","store_id","cate_id","cate_level_id","brand_id","supplier_id","pv_ipv","pv_uv","cart_ipv","cart_uv","collect_uv","num_gmv","amt_gmv","qty_gmv","unum_gmv","amt_alipay","num_alipay","qty_alipay","unum_alipay","ztc_pv_ipv","tbk_pv_ipv","ss_pv_ipv","jhs_pv_ipv","ztc_pv_uv","tbk_pv_uv","ss_pv_uv","jhs_pv_uv","num_alipay_njhs","amt_alipay_njhs","qty_alipay_njhs","unum_alipay_njhs"])
			write.writerow(words)
	else:
		with open(file_name,'a') as f:
			write = csv.writer(f)
			write.writerow(words)
	os.chdir('../../../../code')

def spliteByItem():
	with open("../data4/store/store/5.csv") as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			item_id = row[1]
			# words = [row[0][:4]+"-"+row[0][4:6]+'-'+row[0][6:]] + row[1:]
			writeByItem(item_id,row)
spliteByItem()