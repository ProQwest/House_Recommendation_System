import re
import urllib
import time
import csv



url="http://www.weichert.com/62133837/"
#pagenum=
datalist = []
htmlFile = urllib.urlopen(url)
htmlText = htmlFile.read()

regex = '<h3>Property Information</h3>([^\t]*?)</ul>'
datalist.append(re.compile(regex).findall(htmlText))
print datalist
data = re.sub('<li>(Lot.+?)</li>',"333333",str(datalist))
print data    
htmlFile.close()


