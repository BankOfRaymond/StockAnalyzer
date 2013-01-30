
# stock crawler, get from list of stocks, download historical data
import urllib2


stocks = ["AAPL"]



#for i in range(len(stocks)):


def 
    url = "http://ichart.finance.yahoo.com/table.csv?s="+stocks[i]+"&d=0&e=30&f=2013&g=d&a=8&b=7&c=1984&ignore=.csv"
    response = urllib2.urlopen(url)
    
    localFile = open(stocks[i], 'w')
    localFile.write(response.read())
    localFile.close()



