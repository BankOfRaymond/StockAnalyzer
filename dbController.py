#Connect to DB, and then insert stock 
import MySQLdb
import dbConnect



def connectToDB():
	return MySQLdb.connect(dbConnect.HOST,dbConnect.USERNAME,dbConnect.PASSWORD)
	
def disconnectFromDB(database):
	database.close()

def checkSymbolInDB(symbol):
	return False
	# cursor.execute("search")

#Needs a check to see if already in DB
def insertListOfSymbols(exchange, listOfStocks):
	database = connectToDB()
	for stock in listOfStocks:
		cursor = database.cursor()
		try:	cursor.execute("INSERT INTO Finance.stockList (symbol,name,exchange) VALUES (%s,%s,%s)",(stock[0], stock[1], exchange))
		except MySQLdb.Error, e:	
			print stock[0],stock[1],exchange
			print "Error %d: %s" % (e.args[0], e.args[1])
			cursor.execute("UPDATE Finance.stockList SET symbol=%s, name=%s, exchange=%s",(stock[0],stock[1],exchange))
		database.commit()
	disconnectFromDB(database)


def insertStockPriceIntoDB():
	True
