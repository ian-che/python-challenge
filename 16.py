#!/usr/bin/env python
import os
import urllib
import urllib2
import base64
import xmlrpclib
import datetime
import re, Image
import numpy as np

url = 'http://www.pythonchallenge.com/pc/return/mozart.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
    

mozart = Image.open("mozart.gif")
#mozart.show()
ll = list(mozart.getdata())

np_ary = np.array(ll)
print np_ary.size
np_ary = np.reshape( np_ary, (480,640))
np_ary = np.reshape( np_ary, (480,-1))
print np_ary.size

imdata2 = np.zeros(np_ary.shape)


for y in range( 0, 480, 1):
    for x in range( 0, 640, 1):
        if np_ary[y][x] == 195:
           imdata2[y][0:]=np_ary[y][x:639]
           imdata2[y][639-x:]=np_ary[0:]
#    np_ary[i][i] = i
#    imdata2[i][i] = i

imdata2.shape = (480 * 640, )
mozart.putdata(imdata2)
#np_ary.shape = (480 * 640, )
#mozart.putdata(np_ary)
#mozart.show()


a = range(6)
print a
print np.reshape( a, (2,3))
print np.reshape( a, (3,2))

