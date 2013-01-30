
#This will calculate the BETA given a list of EOD data


AAPL = [1.0,2.0,3.0] #,4,5,6,7,8,9,10]
SNP  = [8.0,2.0,3.0]

#Returns list of returns of size n-1
def getReturns(eodData):
  dailyReturns = []
	for i in range(1,len(eodData)):	dailyReturns.append( (eodData[i]-eodData[i-1])/eodData[i-1] )
	return dailyReturns

#Typically Stock1 is the comparing stock. stock2 is the index, or stock to compare against
def calculateBeta(stock1,stock2):
	a 	= getReturns(stock1)
	b 	= getReturns(stock2)
	covariance	= ( 1/(len(a)-1) ) * (  sum([a[i]*b[i] for i in range(len(a))])  -  (sum(a)*sum(b)/len(a))                    )
	variance	= (1/(len(b)-1))  * (  sum([pow(b[i],2) for i in range(len(b))]) - ( pow(sum(b),2) /len(b) )   )
	return covariance /variance

print calculateBeta(AAPL,SNP)
