from sklearn.linear_model import LinearRegression
from sklearn import cross_validation
from sklearn import metrics
from sklearn.feature_selection import f_regression
import pandas as pd
import numpy as np
import csv


def train():
	item = pd.read_csv("../data2/all/item_feature_per15.csv",header=None)
	data = item.iloc[:,2:-1]
	target = item.iloc[:,-1]
	# .3 as test data and 0.7 as train data

	data = data.drop([44,48,50],axis=1)

	X_train,X_test,y_train,y_test = cross_validation.train_test_split(data,target,test_size=0.3,random_state=40)
	model = LinearRegression(normalize=False,copy_X=True)
	model.fit(X_train,y_train)
	# print X_train.shape

	print model.intercept_
	print model.coef_

	# selectModel = SelectFromModel(model,prefit=True)
	# X_new = selectModel.transform(X_train)
	# print X_train.shape
	# print X_new.shape

	# f, pval = f_regression(X_train,y_train,center=True)
	# print "-------------------------"
	# print f
	# print "-------------------------"
	# print pval


	# print np.sqrt(metrics.mean_squared_error(y_test, y_pred))
	# result = zip(y_test,y_pred)
	# print result

	#predict

	allData = pd.read_csv("../data2/all/predict_per15.csv",header=None)
	inData = allData.iloc[:,2:]

	inData = inData.drop([44,48,50],axis=1)
	print inData.shape

	y_pred = model.predict(inData)
	result = zip(allData.iloc[:,1],["all"]*len(y_pred),y_pred)

	with open("../data2/submission_0505_del.csv","a") as f:
		write = csv.writer(f)
		for sample in result:
			sample = list(sample)
			if sample[2] < 0:
				sample[2] = 0
			write.writerow(sample)	

if __name__ == '__main__':
	train()