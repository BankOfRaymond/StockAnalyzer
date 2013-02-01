

# stock crawler, get from list of stocks, download historical data
import urllib2
import os
import csv

stocks = ["AAPL"]





#for i in range(len(stocks)):


#def getHistorical(stock):
for i in range(1):
	directory = "./stockHistorical/"
	#directory = "stockHistorical"
	if not os.path.exists(directory):
		os.makedirs(directory)



	stock = "AAPL"  # Temporary place holder to set values

	
	#Dependent on Yahoo finance to get historical data
	url = "http://ichart.finance.yahoo.com/table.csv?s="+stock+"&d=0&e=30&f=2013&g=d&a=8&b=7&c=1984&ignore=.csv"
	response = urllib2.urlopen(url)
	localFile = open(directory+stock, 'w')
	localFile.write(response.read())
	localFile.close()
	filereader = csv.reader(open(directory+stock,'rb'), delimiter=",")
	
	#setup variables
	#Name of Stock
	#Date,Open,High,Low,Close,Volume,Adj Close
	for document in filereader:
		name 		= stock
		date 		= document[0]
		openPrice 	= document[1]
		highPrice	= document[2]
		lowPrice	= document[3]
		closingPrice= document[4]
		volume 		= document[5]
		adjClose	= document[6]

		print "Name: "+stock+ " date "+ date + " closingPrice " + closingPrice





#print getHistorical("AAPL")


