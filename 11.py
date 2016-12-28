#!/usr/bin/env python
import os
import urllib
import urllib2
import base64

import re, Image

url = 'http://www.pythonchallenge.com/pc/return/5808.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg','cave.jpg')

cave = Image.open("cave.jpg")
cave.show()

ll = list(cave.getdata())

#print ll

odd =  [ ll[x] for x in range( 1, len(ll), 2) ]
even = [ ll[x] for x in range( 0, len(ll), 2) ]

im_sz = cave.size;


im2 = Image.new(cave.mode, cave.size)
im2.putdata(odd+even)

im2.show()
