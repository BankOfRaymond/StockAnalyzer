#1) Looks at what CSV files are in ./stockSymbolList Directory and looks for files of stocks
#2) Iterates through the "list of exchanges" 
#3) parses in CSV and gets list of stocks
#4) Connects to DB and inserts stocks into DB, then disconnects at end

import csv
from os import listdir
from os.path import isfile, join
import dbController		#controls the inserting of into MYSQL

#goes into directory specified, and pulls all *.csv files of each exchange
def getListOfExchanges(directory):
	return [ f for f in listdir(directory) if isfile(join(directory,f)) ]

def getListOfStocks(directory, exchangeFile):
	listOfStocks = []
	fileReader = csv.reader(open(directory+exchangeFile), delimiter=",")
	firstRow = True  		#Allows program to skip the first row of csv
	for line in fileReader:
		if firstRow == True:	firstRow = False
		else:
			stock = line[0].split('\t')
			symbol = stock[0]
			companyName = stock[1]
			listOfStocks.append([symbol, companyName])
	return listOfStocks

dirExchanges = "./stockSymbolList/"  #Where the exchange directory is stored
listOfExchanges = getListOfExchanges(dirExchanges)
for i in range(len(listOfExchanges)):
	exchange = listOfExchanges[i].split(".")[0]
	listOfStocks = getListOfStocks(dirExchanges,listOfExchanges[i])
	dbController.insertListOfSymbols(exchange, listOfStocks)
