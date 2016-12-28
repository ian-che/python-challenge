#!/usr/bin/env python
import os
import urllib
import urllib2



content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read()
print content

#content = urllib.urlopen("http://www.pythonchallenge.com/pc/return/good.html").read()
#print content

#un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

import bz2

un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!" \
     "\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!" \
     "\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

aaa = [bz2.decompress(elt) for elt in (un, pw)]

print aaa[0], aaa[1]


url = 'http://www.pythonchallenge.com/pc/return/good.html'

import base64
base64string = base64.encodestring('%s:%s' % (aaa[0], aaa[1]))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
