from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn import metrics
import pandas as pd
import numpy as np
import csv


def train():
	item = pd.read_csv("../data2/store/item_feature_per10.csv")
	data = item.iloc[:,3:-1]
	target = item.iloc[:,-1]
	# .3 as test data and 0.7 as train data
	X_train,X_test,y_train,y_test = cross_validation.train_test_split(data,target,test_size=0.3,random_state=40)
	model = LinearRegression(normalize=True,copy_X=True)
	model.fit(X_train,y_train)
	# print X_train.shape

	# print model.intercept_
	# print model.coef_

	# print np.sqrt(metrics.mean_squared_error(y_test, y_pred))
	# result = zip(y_test,y_pred)
	# print result

	#predict

	allData = pd.read_csv("../data2/store/storepredict_per10.csv")
	inData = allData.iloc[:,3:]
	print inData.shape

	y_pred = model.predict(inData)
	result = zip(allData.iloc[:,1],allData.iloc[:,2],y_pred)

	with open("../data2/submission_per10.csv","a") as f:
		write = csv.writer(f)
		for sample in result:
			sample = list(sample)
			if sample[2] < 0:
				sample[2] = 0
			sample[2] *= 2
			write.writerow(sample)	

if __name__ == '__main__':
	train()