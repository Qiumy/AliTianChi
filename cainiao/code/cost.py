import csv

def calCost(predict, fact, config):
	predictData = {}
	with open(predict,'rb') as f:
		rows = csv.reader(f)
		for row in rows:
			predictData[(row[0],row[1])] = int(row[2])

	factData = {}
	with open(fact,'rb') as f:
		rows = csv.reader(f)
		for row in rows:
			factData[(row[0],row[1])] = int(row[2])
	print len(factData)

	configData = {}
	with open(config,'rb') as f:
		rows = csv.reader(f)
		rows.next()
		for row in rows:
			a, b = row[2].split('_')
			configData[(row[0],row[1])] = (float(a),float(b))

	costSum = 0

	cnt = 0
	for sample in factData:
		cnt += 1
		if sample in predictData:
			if factData[sample] > predictData[sample]:
				costSum += (factData[sample] - predictData[sample])*configData[sample][0]
			else:
				costSum += (predictData[sample] - factData[sample])*configData[sample][1]
		else:
			costSum += factData[sample]*configData[sample][0]
			costSum += factData[sample]*configData[sample][1]
	print cnt
	return costSum

print calCost("../data/pre0420/predict_test.csv","../data/pre0420/fact_test.csv","../data/pre0420/config1.csv")