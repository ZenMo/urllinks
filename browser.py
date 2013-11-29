## Python Web Browser

import urllib
from bs4 import BeautifulSoup
url = 'http://gizmodo.com/comet-ison-may-still-be-alive-1473478801'
fhand1 = urllib.urlopen(url)
fhand2 = urllib.urlopen(url)

print fhand1,'\n'

line_count = 0
for line in fhand1:
    line_count+=1

rdata = fhand2.read()
soup2 = BeautifulSoup(rdata)

cut = 0
if cut==1:
    cut_data = rdata[:3000]
    print cut_data,'\n'
elif cut==2:
    print rdata
else:
    print
    
array = []
char_count = 0

print soup2.title.get_text(),'\n'
for para in soup2.find_all("p"):
    print para.get_text(),'\n'
    array.append(para.get_text())
for p in array:
    for char in p:
        char_count+=1
#print soup2.get_text(),'\n'

print '"p" tags: ', len(array),'\n'
print 'Lines: ',line_count,'\n'
print 'Charater count: ', char_count,'\n'
print 'All characters in HTML: ',len(rdata),'\n'
