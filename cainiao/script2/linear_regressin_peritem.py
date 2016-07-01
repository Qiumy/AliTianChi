from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn import metrics
import pandas as pd
import numpy as np
import csv


result = []

def train():
	item = pd.read_csv("../data2/store/item_feature.csv",usecols=[0]+range(2,56),index_col=[0,1],header=None)
	preData = pd.read_csv("../data2/store/storepredict2.csv",usecols=range(1,55),index_col=[0,1],header=None) 
	index = set(item.index)

	preIndex = set(preData.index)
	for idx in index:
		model = LinearRegression(normalize=True,copy_X=True)
		if type(item.ix[idx][55]) == np.float64:
			result.append([idx[0],idx[1],item.ix[idx][55]])
		else:
			model.fit(item.ix[idx][range(3,55)],item.ix[idx][55].tolist())

			if idx in preIndex:
				preFeature = preData.ix[idx][range(3,55)]
				pre = model.predict(preFeature)
				result.append([idx[0],idx[1],pre[0]])
			else:
				result.append([idx[0],idx[1],0])
		
	with open("../data2/submission4.csv","a") as f:
		write = csv.writer(f)
		for sample in result:
			if sample[2] < 0:
				sample = list(sample)
				sample[2] = 0
			write.writerow(sample)	

if __name__ == '__main__':
	train()