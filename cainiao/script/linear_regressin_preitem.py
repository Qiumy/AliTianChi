from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn import metrics
import pandas as pd
import numpy as np
import csv

result = []
def train():
	item = pd.read_csv("../data2/all/item_feature4.csv",usecols=[0]+range(2,55),index_col=0,header=None)
	preData = pd.read_csv("../data2/all/predict2.csv",usecols=range(1,54),index_col=0,header=None) 
	index = set(item.index)
	preIndex = set(preData.index)
	for idx in index:
		model = LinearRegression(normalize=True,copy_X=True)
		if type(item.ix[idx][54]) == np.float64:
			result.append([idx,"all",item.ix[idx][54]])
		else:
			model.fit(item.ix[idx][range(2,54)],item.ix[idx][54].tolist())
			# print preData.iloc[203]
			# return
			if idx in preIndex:
				preFeature = preData.ix[idx][range(2,54)]
				try:
					pre = model.predict(preFeature)
				except Exception as e:
					print e
					print preFeature
				result.append([idx,"all",pre[0]])
			else:
				result.append([idx,"all",0])
		
	with open("../data2/submission4.csv","a") as f:
		write = csv.writer(f)
		for sample in result:
			if sample[2] < 0:
				sample = list(sample)
				sample[2] = 0
			write.writerow(sample)	

if __name__ == '__main__':
	train()