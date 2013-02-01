#put stock in DB

import MySQLdb
import csv
from os import listdir
from os.path import isfile, join

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

#Connect to DB, and then insert stock 
def insertStockIntoDB(exchange, stock, database):
	cursor = database.cursor()
	try:	cursor.execute("INSERT INTO Finance.stockList (symbol,name,exchange) VALUES (%s,%s,%s)",(stock[0], stock[1], exchange))
	except MySQLdb.Error, e:	
		print "Error %d: %s" % (e.args[0], e.args[1])
		cursor.execute("UPDATE Finance.stockList SET symbol=%s, name=%s, exchange=%s",(stock[0],stock[1],exchange))
	database.commit()

def connectToDB():
	import dbConnect
	return MySQLdb.connect(dbConnect.HOST,dbConnect.USERNAME,dbConnect.PASSWORD)
	
def disconnectFromDB(database):
	database.close()



#1) Looks at what CSV files are in ./stockSymbolList Directory and looks for files of stocks
#2) Iterates through the "list of exchanges" 
#3) parses in CSV and gets list of stocks
#4) Connects to DB and inserts stocks into DB, then disconnects at end
dirExchanges = "./stockSymbolList/"  #Where the exchange directory is stored
listOfExchanges = getListOfExchanges(dirExchanges)
for i in range(len(listOfExchanges)):
	database = connectToDB()
	exchange = listOfExchanges[i].split(".")[0]
	listOfStocks = getListOfStocks(dirExchanges,listOfExchanges[i])
	for stock in listOfStocks:
		insertStockIntoDB(exchange, stock, database)
	disconnectFromDB(database)
