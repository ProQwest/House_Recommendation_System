import re
import urllib
import time
import csv

url="http://www.weichert.com/61963111/"
# url = "http://finance.yahoo.com/q/is?s=AAPL"

datalist=[]
htmlFile=urllib.urlopen(url)
htmlText=htmlFile.read()

# regex = '<h3>Property Information</h3>' + '\n.*' + '<ul>(.*)MLS/Web'
#regex = '<h3>Property Information</h3>.*\n.*\n<ul>.*\n.*\n' + '.*<li>(.*)</li>.*\n.*\n' * 12
regex = '<h3>Property Information</h3>([^\t]*?)</ul>'
# regex = '<h3>Property Information</h3>\n.*'
datalist.append(re.compile(regex).findall(htmlText))

htmlFile.close()
print datalist
