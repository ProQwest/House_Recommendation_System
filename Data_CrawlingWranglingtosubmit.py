import re
import urllib
import time
import csv

def getdata(num):
    datalist = []
    htmlFile = urllib.urlopen(url)
    htmlText = htmlFile.read()
  #  regex = '<h3>Property Information</h3>' + '\n.*' + '<ul>(.*)MLS/Web'
# regex = '<h3>Property Information</h3>.*\n.*\n<ul>.*\n.*\n' + '.*<li>(.*)</li>.*\n.*\n' * 12
    regex = '<h3>Property Information</h3>([^\t]*?)</ul>'

    datalist.append(re.compile(regex).findall(htmlText))
    datalist = re.sub(',', "", str(datalist))
    datalist = re.sub(' ', "", str(datalist))
   # print datalist
    datalist = re.sub('(Fees.+?)</li>', "", str(datalist))
    finallist = []
    if  re.findall(r'Commercial', str(datalist))==[]:
        price = re.findall(r'\$+(\d+)</li>+', str(datalist))
        if len(price) == 2:
            for i in price:finallist.append(i)
            year = re.findall(r"Builtin(.+?)</li>", str(datalist))
            if year != []:
                finallist.append(year[0])
                bedroom = re.findall(r'<li>+(\d+)Bedroom+', str(datalist))
                if bedroom != []:
                    finallist.append(bedroom[0])
                bathroom = re.findall(r'<li>+(\d+)FullBath', str(datalist))
                halfbathroom = re.findall(r'Bath+(\d+)HalfBath', str(datalist))
                if bathroom != []:
                    if halfbathroom != []:
                        finallist.append(bathroom[0]+'.'+halfbathroom[0])
                    else:
                        finallist.append(bathroom[0])
                lot = re.findall(r'Lots', str(datalist))
                if lot != []:finallist.append('1')
                else:finallist.append('0')
           # # print datalist
           #  datalist = re.sub('(MLS.+?)</li>', "", str(datalist))
           #  datalist = re.sub('(Unit.+?)</li>', "", str(datalist))
           # # datalist = re.sub('<li>(.+?)Story</li>', "", str(datalist))
           #  datalist = re.sub('(ID.+?)</li>', "", str(datalist))
           #  datalist = re.sub(r'<li>+(\d+)Square+', "", str(datalist))
           #  datalist = re.sub(r'<li>+(\d+)Story+', "", str(datalist))
            #datalist = re.sub('<li>(Taxes.+?)</li>', "", str(datalist))
            # final = datafile.read()
            # final.replace('\r','')
    textlist = datalist_clean(datalist)
  #  print textlist
    htmlFile.close()
    return finallist,textlist

def datalist_clean(datalist):
    with open(test, "w") as w:
            w.write(str(datalist))
    with open(test, "r") as r:
            data = r.read()
        #    print type(data)
            data = data.replace('\\r\\n','')
            data = data.replace('<ul>', '')

            data = data.replace('[[\'', '')
            data = data.replace('\']]', '')
            data = data.replace(' ','')
            data = data.replace(',', '')
            data = data.replace('/', '')
            data = data.replace('-', '')
          #  data = data.replace('$', '')
            data = data.replace('Commercial','*')
            data = data.split("<li>")
        #     data = [x for x in data if x != '']
        #     a = 1
        #     for x in data:
        #         if 'Tax' in x:
        #             a = 0
        #     if a:
        #         data.insert(3,0)
        #     datastr = str(data)
        #     print datastr
        #     for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        #         datastr = datastr.replace(i,'')
        #     print datastr
         #   data = datastr.split(","
          #  dataclean2(data)
            data = [x for x in data if x != '']
    return data

test = "test.csv"
test2 = "test2.csv"
commercial = "commercial.csv"
house = "house.csv"

with open(house,"ab+") as h:
        h_csv = csv.writer(h)
        title = ['price','tax','year','bedroom','bathroom','lot','address','textinfo']
   #     h_csv.writerow(title)
        for a in range(3510,3800):
            num = str(a)
            url = "http://www.weichert.com/6317" + num
            finallist,textlist = getdata(url)
            if len(finallist)==6:
                finallist.append(url)
                finallist = finallist + textlist
                h_csv.writerow(finallist)
