import os
import csv

def getLast2Weekall():
	all_item = {}
	direction = "../data4/all/date/"
	file_list = os.listdir(direction)

	for file_name in file_list:
		if "20151228" > file_name > "20151214" :
			print file_name
			file_path = direction+file_name
			rows = csv.reader(open(file_path,"rb"))
			rows.next()
			for row in rows:
				if (row[1],"all") not in all_item:
					all_item[(row[1],"all")] = int(row[-2])
				else:
					all_item[(row[1],"all")] += int(row[-2])
	with open("../data4/fact_test0509.csv", 'wb') as f:
		write = csv.writer(f)
		for sample in all_item:
			write.writerow([sample[0],sample[1],all_item[sample]])
getLast2Weekall()

def getLast2Weekstore():
	all_item = {}
	direction = "../data4/store/date/"
	file_list = os.listdir(direction)

	for file_name in file_list:
		if "20151228" > file_name > "20151214" :
			print file_name
			file_path = direction+file_name
			rows = csv.reader(open(file_path,"rb"))
			rows.next()
			for row in rows:
				if (row[1],row[2]) not in all_item:
					all_item[(row[1],row[2])] = int(row[-2])
				else:
					all_item[(row[1],row[2])] += int(row[-2])
	with open("../data4/fact_test0509.csv", 'a') as f:
		write = csv.writer(f)
		for sample in all_item:
			write.writerow([sample[0],sample[1],all_item[sample]])
getLast2Weekstore()