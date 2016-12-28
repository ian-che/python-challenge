#!/usr/bin/env python
import os
import urllib
import urllib2
import base64
import xmlrpclib
import datetime
import re, Image

url = 'http://www.pythonchallenge.com/pc/return/uzi.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

#urllib.urlretrieve('http://huge:file@www.pythonchallenge.com/pc/return/wire.png','wire.png')
    


import calendar
for i in range(1006, 2006, 10):
  if calendar.weekday( i, 1, 26) == 0:
       print i

print [i for i in range(1006, 2006, 10) if calendar.weekday(i, 1, 1) == 3][-3]
