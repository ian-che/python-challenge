#!/usr/bin/env python
import os
import urllib
import urllib2
import base64
import xmlrpclib
import datetime
import re, Image

url = 'http://www.pythonchallenge.com/pc/return/italy.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

#urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/wire.png','wire.png')

img = Image.open("wire.png")
print img.size
#img.show()


ll = list(img.getdata())

im = Image.new(img.mode, (100,100))
im.putdata(ll)
im.show()



xx = [(0,255,0)]*10000

n = 0
x = y = 0
z = 0
for i in range(100,0,-2):
    print i, i-1, i-1, i-2
    n = n + (i + i-1 + i-1 +i-2)

    for j in range( 0, i, 1):        
        xx[x + (y+j)*100] = ll[z+j]
        #z += 1
    z = z + j + 1
    y = y + j
    x = x + 1


    for j in range( 0, i-1, 1):        
        xx[x+j + y*100] = ll[z]
        z += 1
    x = x + j
    y = y - 1

    for j in range( 0, i-1, 1):        
        xx[x + (y-j)*100] = ll[z]
        z += 1
    y = y - j
    x = x - 1 


    for j in range( 0, i-2, 1):        
        xx[x - j + y*100] = ll[z]
        z += 1
    x = x - j
    y = y + 1

#print n



im2 = Image.new(img.mode, (100,100))
im2.putdata(xx)
im2.show()


