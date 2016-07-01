from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn import metrics
import pandas as pd
import numpy as np
import csv


def train():
	item = pd.read_csv("../data2/store/item_feature_per10.csv", usecols=[0]+range(2,51), index_col=[1], header=None)
	preData = pd.read_csv("../data2/store/storepredict_per10.csv", usecols=range(1,50),index_col=[1],header=None)

	index = set(item.index)

	for idx in index:
		model = LinearRegression(normalize=True,copy_X=True)
		model.fit(item.ix[idx][range(3,50)],item.ix[idx][50])

		storeFeature = preData.ix[idx][range(3,50)]
		pre = model.predict(storeFeature)
		storeResult = zip(preData.ix[idx][1],[idx]*len(storeFeature),pre)
		writeResult(storeResult)



def writeResult(result):
	with open("../data2/submission_0505_per10.csv","a") as f:
		write = csv.writer(f)
		for sample in result:
			sample = list(sample)
			if sample[2] < 0:
				sample[2] = 0
			sample[2] *= 2
			write.writerow(sample)	

if __name__ == '__main__':
	train()