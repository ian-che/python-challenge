#!/usr/bin/env python

import urllib
import pickle



#content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/peak.html").read()
#print content


obj = pickle.load(open("banner.p", "r"))

#print obj[1][3][0]

for row in obj:
    #print row
    s = "x"
    for col in row:
        #print col
        s = s + col[0]*col[1]
    print s
