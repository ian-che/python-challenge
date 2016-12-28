#!/usr/bin/env python
import os
import urllib
import urllib2
import base64

import re, Image

url = 'http://www.pythonchallenge.com/pc/return/evil.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page


urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil1.jpg','evil1.jpg')
urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil2.jpg','evil2.jpg')
urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx','evil2.gfx')
urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil3.jpg','evil3.jpg')
urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/evil4.jpg','evil4.jpg')

img = Image.open("evil1.jpg")
#img.show()
ll = list(img.getdata())


im_sz = img.size;
f = open("evil2.gfx", "r")
gfx = f.read()
f.close()
print len(gfx)


for i in range(5):  
    file = open("evil_0%d.jpg" % i, "wb")  
    file.write(gfx[i::5])  
    file.close()  

'''
for x in range( 0, len(gfx), 3):
    ll[x] = 0# ( gfx[x+0], gfx[x+1], gfx[x+2])


im2 = Image.new(img.mode, im_sz)
im2.putdata(ll)
im2.show()


im_sz = evil1.size;
print im_sz

sub = []
for y in range(0, im_sz[1]-3, 3):
    sub += [ ll[    y*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]    


for y in range(1, im_sz[1]-3, 3):
    sub += [ ll[    y*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]    


#for y in range(2, im_sz[1]-3, 3):
#    sub += [ ll[    y*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 0, im_sz[0], 2) ]    

for y in range(0, im_sz[1]-3, 3):
    sub += [ ll[    y*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]    


for y in range(1, im_sz[1]-3, 3):
    sub += [ ll[    y*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]    


#for y in range(2, im_sz[1]-3, 3):
#    sub += [ ll[    y*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]
#    sub += [ ll[(y+1)*im_sz[0]+x] for x in range( 1, im_sz[0], 2) ]    


im2 = Image.new(evil1.mode, (320,180*4))
im2.putdata(sub)
im2.show()

'''
