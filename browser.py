## Python Web Browser

import urllib
from bs4 import BeautifulSoup

fhand1 = urllib.urlopen('http://www.google.com/')
fhand2 = urllib.urlopen('http://www.google.com/')

print fhand1,'\n'

line_count = 0
for line in fhand1:
    line_count+=1

rdata = fhand2.read()
cut_data = rdata[:3000]

soup = BeautifulSoup(fhand1)
soup2 = BeautifulSoup(rdata)
data = soup.prettify()

print cut_data,'\n'
print 'Charaters Shown: 3000\n'
print 'Characters: ',len(rdata),'\n'
print 'Lines: ',line_count,'\n'
print
