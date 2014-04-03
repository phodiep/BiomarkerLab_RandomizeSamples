from random import shuffle
import csv

filename = raw_input('File to randomize:')
data = list()

with open(filename+'.csv',"rb") as csvFile:
	for line in csv.reader(csvFile): data += line[0],

shuffle(data)

with open(filename+'_random.csv','wb') as exportFile:
	dataExport = csv.writer(exportFile, delimiter=',',quoting=csv.QUOTE_ALL)
	for line in data: dataExport.writerow([line])
