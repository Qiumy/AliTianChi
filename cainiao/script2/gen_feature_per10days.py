import csv
import pandas as pd
import datetime
import numpy as np
import os

date_id = ["20141101","20141110","20141120","20141201","20141210","20141220",\
		   "20150101","20150110","20150120","20150301","20150310","20150320",\
		   "20150401","20150410","20150420","20150501","20150510","20150520",\
		   "20150601","20150610","20150620","20150701","20150710","20150720",\
		   "20150801","20150810","20150820","20150901","20150910","20150920",\
		   "20151001","20151010","20151020","20151101","20151110","20151120"]
store_id = ["1","2","3","4","5"]
features = []
def calFeature():
	for store in store_id:
		direction = "../data2/store/store/"+store
		file_list = os.listdir(direction)
		for file_name in file_list:
			cinData(file_name,store)

def cinData(itemID,storeID):
	item = pd.read_csv("../data2/store/store/"+storeID+'/'+itemID)
	itemID = itemID[:-4]
	# try:
	# 	item2 = []
	# 	x = None
	# 	for x in item['date']:
	# 		item2.append(datetime.datetime.strptime(x, "%Y-%m-%d"))
	# 	item['date'] = item2
	# except Exception as e:
	# 	print x
	# 	print e


	item["date"] = [datetime.datetime.strptime(x, "%Y-%m-%d") for x in item['date']]
	itemsort = item.sort_values(by="date")
	for date in date_id:
		begindate = datetime.datetime.strptime(date, "%Y%m%d")
		enddate = datetime.datetime.strptime(date, "%Y%m%d") + datetime.timedelta(days=9)
		boolArr = [ begindate<=x<=enddate for x in itemsort["date"]]
		monthdata = itemsort[boolArr]
		monthdata = addZero(itemID, date, monthdata)

		afterSet = genAfterNDaysDateSet(enddate,7)
		boolArr = [ x in afterSet for x in itemsort["date"]]
		afterData = itemsort[boolArr]["qty_alipay_njhs"].sum()
		genFeature(itemID,date,storeID,monthdata,afterData)

def addZero(itemID,dateID,monthdata):
	if monthdata.shape[0] == 10:
		return monthdata
	else:
		date = datetime.datetime.strptime(dateID, "%Y%m%d")
		a_day = datetime.timedelta(days=1)
		dateRange = []
		for i in range(10):
			dateRange.append(date)
			date += a_day
		monthdata = monthdata.reindex(dateRange,fill_value=0)
		monthdata["date"] = dateRange
		return monthdata

def genFeature(itemID,dateID,storeID,monthdata,afterData):
	itemFeatureList = []

	sum_pv_uv = monthdata["pv_uv"].sum()
	mean_pv_uv = monthdata["pv_uv"].mean()
	quantile25_pv_uv = monthdata["pv_uv"].quantile(q=0.25)
	median_pv_uv = monthdata["pv_uv"].median()
	quantile75_pv_uv = monthdata["pv_uv"].quantile(q=0.75)
	var_pv_uv = monthdata["pv_uv"].var()
	max_min_pv_uv = monthdata["pv_uv"].max()-monthdata["pv_uv"].min()

	sum_cart_ipv = monthdata["cart_ipv"].sum()
	mean_cart_ipv = monthdata["cart_ipv"].mean()
	quantile25_cart_ipv = monthdata["cart_ipv"].quantile(q=0.25)
	median_cart_ipv = monthdata["cart_ipv"].median()
	quantile75_cart_ipv = monthdata["cart_ipv"].quantile(q=0.75)
	var_cart_ipv = monthdata["cart_ipv"].var()
	max_min_cart_ipv = monthdata["cart_ipv"].max()-monthdata["cart_ipv"].min()

	sum_collect_uv = monthdata["collect_uv"].sum()
	mean_collect_uv = monthdata["collect_uv"].mean()
	quantile25_collect_uv = monthdata["collect_uv"].quantile(q=0.25)
	median_collect_uv = monthdata["collect_uv"].median()
	quantile75_collect_uv = monthdata["collect_uv"].quantile(q=0.75)
	var_collect_uv = monthdata["collect_uv"].var()
	max_min_collect_uv = monthdata["collect_uv"].max()-monthdata["collect_uv"].min()

	sum_jhs_pv_ipv = monthdata["jhs_pv_ipv"].sum()
	mean_jhs_pv_ipv = monthdata["jhs_pv_ipv"].mean()
	quantile25_jhs_pv_ipv = monthdata["jhs_pv_ipv"].quantile(q=0.25)
	median_jhs_pv_ipv = monthdata["jhs_pv_ipv"].median()
	quantile75_jhs_pv_ipv = monthdata["jhs_pv_ipv"].quantile(q=0.75)
	var_jhs_pv_ipv = monthdata["jhs_pv_ipv"].var()
	max_min_jhs_pv_ipv = monthdata["jhs_pv_ipv"].max()-monthdata["jhs_pv_ipv"].min()

	sum_qty_alipay = monthdata["qty_alipay"].sum()
	mean_qty_alipay = monthdata["qty_alipay"].mean()
	quantile25_qty_alipay = monthdata["qty_alipay"].quantile(q=0.25)
	median_qty_alipay = monthdata["qty_alipay"].median()
	quantile75_qty_alipay = monthdata["qty_alipay"].quantile(q=0.75)
	var_qty_alipay = monthdata["qty_alipay"].var()
	max_min_qty_alipay = monthdata["qty_alipay"].max()-monthdata["qty_alipay"].min()

	sum_qty_gmv = monthdata["qty_gmv"].sum()
	mean_qty_gmv = monthdata["qty_gmv"].mean()
	quantile25_qty_gmv = monthdata["qty_gmv"].quantile(q=0.25)
	median_qty_gmv = monthdata["qty_gmv"].median()
	quantile75_qty_gmv = monthdata["qty_gmv"].quantile(q=0.75)
	var_qty_gmv = monthdata["qty_gmv"].var()
	max_min_qty_gmv = monthdata["qty_gmv"].max()-monthdata["qty_gmv"].min()

	itemFeatureList = [itemID,dateID,storeID,\
						sum_pv_uv,mean_pv_uv,quantile25_pv_uv,median_pv_uv,quantile75_pv_uv,var_pv_uv,max_min_pv_uv,\
						sum_cart_ipv,mean_cart_ipv,quantile25_cart_ipv,median_cart_ipv,quantile75_cart_ipv,var_cart_ipv,max_min_cart_ipv,\
						sum_collect_uv,mean_collect_uv,quantile25_collect_uv,median_collect_uv,quantile75_collect_uv,var_collect_uv,max_min_collect_uv,\
						sum_qty_gmv,mean_qty_gmv,quantile25_qty_gmv,median_qty_gmv,quantile75_qty_gmv,var_qty_gmv,max_min_qty_gmv,\
						sum_qty_alipay,mean_qty_alipay,quantile25_qty_alipay,median_qty_alipay,quantile75_qty_alipay,var_qty_alipay,max_min_qty_alipay,\
						sum_jhs_pv_ipv,mean_jhs_pv_ipv,quantile25_jhs_pv_ipv,median_jhs_pv_ipv,quantile75_jhs_pv_ipv,var_jhs_pv_ipv,max_min_jhs_pv_ipv
					  ]


	# genTrendFeature
	sum5_collect_uv = sum(monthdata["collect_uv"][:5])
	sum10_collect_uv = sum(monthdata["collect_uv"][5:10])

	sum5_cart_ipv = sum(monthdata["cart_ipv"][:5])
	sum10_cart_ipv = sum(monthdata["cart_ipv"][5:10])

	sum5_pv_uv = sum(monthdata["pv_uv"][:5])
	sum10_pv_uv = sum(monthdata["pv_uv"][5:10])

	sum5_qty_gmv = sum(monthdata["qty_gmv"][:5])
	sum10_qty_gmv = sum(monthdata["qty_gmv"][5:10])

	sum5_qty_alipay = sum(monthdata["qty_alipay"][:5])
	sum10_qty_alipay = sum(monthdata["qty_alipay"][5:10])

	trendFeature = [sum10_pv_uv-sum5_pv_uv,\
					sum10_cart_ipv-sum5_cart_ipv,\
					sum10_collect_uv-sum5_collect_uv,\
					sum10_qty_gmv-sum5_qty_gmv,\
					sum10_qty_alipay-sum5_qty_alipay
					]

	itemFeatureList += trendFeature

	itemFeatureList += [afterData]
	features.append(itemFeatureList)
	writeData(itemFeatureList)

def writeData(itemFeatureList):
	with open("../data2/store/item_feature_per10.csv", "a") as f:
		write = csv.writer(f)
		if itemFeatureList[3]!=0:
			write.writerow(itemFeatureList)
		# for feature in features:
		# 	if feature[3]!=0:
		# 		write.writerow(feature)

def genAfterNDaysDateSet(date,n):
	#not inclue date
	dateSet = []
	a_day = datetime.timedelta(days=1)
	tmpdate = date+a_day
	for i in range(n):
		dateSet.append(tmpdate)
		tmpdate += a_day
	return dateSet

if __name__ == '__main__':
	calFeature()
	# writeData()