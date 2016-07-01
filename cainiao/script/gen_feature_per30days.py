import csv
import pandas as pd
import datetime
import numpy as np
import os

date_id = ["201411","201412","201501","201503","201504","201505","201506","201507","201508","201509","201510","201511"]
def calFeature():
	direction = "../data2/all/item"
	file_list = os.listdir(direction)
	for file_name in file_list:
		cinData(file_name)

def cinData(itemID):
	item = pd.read_csv("../data2/all/item/"+itemID)
	itemID = itemID[:-4]
	item["date"] = [datetime.datetime.strptime(x, "%Y-%m-%d") for x in item['date']]
	itemsort = item.sort_values(by="date")
	for date in date_id:
		begindate = datetime.datetime.strptime(date, "%Y%m")
		enddate = datetime.datetime.strptime(date+"30", "%Y%m%d")
		boolArr = [ begindate<=x<=enddate for x in itemsort["date"]]
		monthdata = itemsort[boolArr]
		monthdata = addZero(itemID, date, monthdata)

		afterSet = genAfterNDaysDateSet(enddate,14)
		boolArr = [ x in afterSet for x in itemsort["date"]]
		afterData = itemsort[boolArr]["qty_alipay_njhs"].sum()
		genFeature(itemID,date,monthdata,afterData)

def addZero(itemID,dateID,monthdata):
	if monthdata.shape[0] == 30:
		return monthdata
	else:
		date = datetime.datetime.strptime(dateID, "%Y%m")
		enddate = datetime.datetime.strptime(dateID+"30", "%Y%m%d")
		a_day = datetime.timedelta(days=1)
		dateRange = []
		for i in range(30):
			dateRange.append(date)
			date += a_day
		monthdata = monthdata.reindex(dateRange,fill_value=0)
		monthdata["date"] = dateRange
		return monthdata

def genFeature(itemID,dateID,monthdata,afterData):
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

	itemFeatureList = [itemID,dateID,\
						sum_pv_uv,mean_pv_uv,quantile25_pv_uv,median_pv_uv,quantile75_pv_uv,var_pv_uv,max_min_pv_uv,\
						sum_cart_ipv,mean_cart_ipv,quantile25_cart_ipv,median_cart_ipv,quantile75_cart_ipv,var_cart_ipv,max_min_cart_ipv,\
						sum_collect_uv,mean_collect_uv,quantile25_collect_uv,median_collect_uv,quantile75_collect_uv,var_collect_uv,max_min_collect_uv,\
						sum_qty_gmv,mean_qty_gmv,quantile25_qty_gmv,median_qty_gmv,quantile75_qty_gmv,var_qty_gmv,max_min_qty_gmv,\
						sum_qty_alipay,mean_qty_alipay,quantile25_qty_alipay,median_qty_alipay,quantile75_qty_alipay,var_qty_alipay,max_min_qty_alipay,\
						sum_jhs_pv_ipv,mean_jhs_pv_ipv,quantile25_jhs_pv_ipv,median_jhs_pv_ipv,quantile75_jhs_pv_ipv,var_jhs_pv_ipv,max_min_jhs_pv_ipv
					  ]


	# genTrendFeature
	sum10_collect_uv = sum(monthdata["collect_uv"][:10])
	sum20_collect_uv = sum(monthdata["collect_uv"][10:20])
	sum30_collect_uv = sum(monthdata["collect_uv"][20:])

	sum10_cart_ipv = sum(monthdata["cart_ipv"][:10])
	sum20_cart_ipv = sum(monthdata["cart_ipv"][10:20])
	sum30_cart_ipv = sum(monthdata["cart_ipv"][20:])

	sum10_pv_uv = sum(monthdata["pv_uv"][:10])
	sum20_pv_uv = sum(monthdata["pv_uv"][10:20])
	sum30_pv_uv = sum(monthdata["pv_uv"][20:])

	sum10_qty_gmv = sum(monthdata["qty_gmv"][:10])
	sum20_qty_gmv = sum(monthdata["qty_gmv"][10:20])
	sum30_qty_gmv = sum(monthdata["qty_gmv"][20:])

	sum10_qty_alipay = sum(monthdata["qty_alipay"][:10])
	sum20_qty_alipay = sum(monthdata["qty_alipay"][10:20])
	sum30_qty_alipay = sum(monthdata["qty_alipay"][20:])

	trendFeature = [sum20_pv_uv-sum10_pv_uv,sum30_pv_uv-sum20_pv_uv,\
					sum20_cart_ipv-sum10_cart_ipv,sum30_cart_ipv-sum20_cart_ipv,\
					sum20_collect_uv-sum10_collect_uv,sum30_collect_uv-sum20_collect_uv,\
					sum20_qty_gmv-sum10_qty_gmv,sum30_qty_gmv-sum20_qty_gmv,\
					sum20_qty_alipay-sum10_qty_alipay,sum30_qty_alipay-sum20_qty_alipay
					]

	itemFeatureList += trendFeature

	itemFeatureList += [afterData]
	writeData(itemFeatureList)

def writeData(itemFeatureList):
	with open("../data2/all/item_feature4.csv", "a") as f:
		write = csv.writer(f)
		if itemFeatureList[2]!=0:
			write.writerow(itemFeatureList)

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