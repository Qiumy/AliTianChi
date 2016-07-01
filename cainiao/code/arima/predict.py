import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import csv
import datetime
from statsmodels.graphics.api import qqplot

def predictItem(itemID):
	itemID = "E:/study/tianchi/cainiao/data/all/item/197.csv"
	njhs = []
	dateset = []
	with open(itemID,'rb') as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			date = row[0]
			dateset.append(datetime.datetime.strptime(date[:4]+'-'+date[4:6]+'-'+date[6:],"%Y-%m-%d"))
			njhs.append(float(row[-2]))
	
	# data = pd.Series(njhs,dateset)
	data = pd.DataFrame(njhs)
	data.index = pd.DatetimeIndex(start=dateset[0], end=dateset[-1], freq="D")

	datatrain = data[200:]
	fig = plt.figure(figsize=(12,8))
	ax1=fig.add_subplot(211)
	fig = sm.graphics.tsa.plot_acf(data[200:],lags=40,ax=ax1)
	ax2 = fig.add_subplot(212)
	fig = sm.graphics.tsa.plot_pacf(data[200:],lags=40,ax=ax2)
	# plt.show()

	arma_mod1 = sm.tsa.ARMA(datatrain,(4,0)).fit()
	# print(arma_mod1.aic,arma_mod1.bic,arma_mod1.hqic)
	# arma_mod2 = sm.tsa.ARMA(datatrain,(0,3)).fit()
	# print(arma_mod2.aic,arma_mod2.bic,arma_mod2.hqic)
	# arma_mod3 = sm.tsa.ARMA(datatrain,(4,3)).fit()
	# print(arma_mod3.aic,arma_mod3.bic,arma_mod3.hqic)

	# resid = arma_mod3.resid#残差
	# fig = plt.figure(figsize=(12,8))
	# ax = fig.add_subplot(111)
	# fig = qqplot(resid, line='q', ax=ax, fit=True)
	# plt.show()

	# r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
	# datatrain = np.c_[range(1,41), r[1:], q, p]
	# table = pd.DataFrame(datatrain, columns=['lag', "AC", "Q", "Prob(>Q)"])
	# print(table.set_index('lag'))

	predict_njhs = arma_mod1.predict(datetime.datetime.strptime("2015-12-26","%Y-%m-%d"), datetime.datetime.strptime("2015-12-30","%Y-%m-%d"),dynamic=True)
	print type(predict_njhs)
	fig, ax = plt.subplots(figsize=(12, 8))
	ax = data.ix[datetime.datetime.strptime("2015-01-01","%Y-%m-%d"):].plot(ax=ax)
	predict_njhs.plot(ax=ax)
	plt.show()


predictItem(123)