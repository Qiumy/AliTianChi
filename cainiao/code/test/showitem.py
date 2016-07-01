import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

def showItemFeature(item_id):
	file_path = 'E:/study/tianchi/cainiao/data/all/item/' + str(item_id) + ".csv"
	data = 	pd.read_csv(file_path)
	data = data.sort_values(by = "date")
	# data = data.set_index("date")
	data.index = pd.Index(sm.tsa.datetools.dates_from_range('2001', '2101'))
	data = data.astype(np.float64)

	njhsdata = data["qty_alipay_njhs"]
	# print njhsdata.head()
	

	fig = plt.figure(figsize=(12,8))
	ax1 = fig.add_subplot(211)
	fig = sm.graphics.tsa.plot_acf(njhsdata.values.squeeze(), lags=40, ax=ax1)
	ax2 = fig.add_subplot(212)
	fig = sm.graphics.tsa.plot_pacf(njhsdata, lags=40, ax=ax2)
	# print data.head()
	# print data.describe()

	arma_mod00 = sm.tsa.ARMA(njhsdata, (0,0)).fit()
	# print arma_mod00.params

	arma_mod20 = sm.tsa.ARMA(njhsdata, (2,0)).fit()
	# print arma_mod20.params

	# print arma_mod00.aic, arma_mod00.bic, arma_mod00.hqic
	# print arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic

	fig = plt.figure(figsize=(12,8))
	ax = fig.add_subplot(111)
	ax = arma_mod00.resid.plot(ax=ax);

	resid = arma_mod00.resid


	r,q,p = sm.tsa.acf(resid.values.squeeze(), qstat=True)
	dta = np.c_[range(1,41), r[1:], q, p]
	table = pd.DataFrame(dta, columns=['lag', "AC", "Q", "Prob(>Q)"])
	# print table.set_index('lag')

	predict_sunspots = arma_mod00.predict('2102', '2115', dynamic=True)
	print predict_sunspots
	# plt.show()
showItemFeature(8230)
