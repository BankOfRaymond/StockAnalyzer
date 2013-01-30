
# stock crawler, get from list of stocks, download historical data
import urllib2


stocks = ["AAPL"]


for i in range(len(stocks)):
	url = "http://ichart.finance.yahoo.com/table.csv?s="+stocks[i]+"&d=0&e=30&f=2013&g=d&a=8&b=7&c=1984&ignore=.csv"
	response = urllib2.urlopen(url)


import urllib
urllib.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")
Yet another one, with a "progressbar"

import urllib2

url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()






