import re
def extractData(regex, content, index=1):  
    r = '0'  
    p = re.compile(regex)  
    m = p.search(content)  
    if m:  
        r = m.group(index)  
    return r  
  
regex = r'第(.*)场雪'  
content = '2002年的第一场雪'  
index = 1  
print (extractData(regex, content, index) ) 

