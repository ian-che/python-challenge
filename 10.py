#!/usr/bin/env python
import os
import urllib
import urllib2
import base64

url = 'http://www.pythonchallenge.com/pc/return/bull.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page



# len(a[30]) = ?
# a = [1, 11, 21, 1211, 111221, 
# fa


def lookNsay(look):
    count = 1 
    last_c = look[0]
    say = ''
    for c in look[1:len(look)]:
        if c == last_c:
           count = count + 1
        else:
           say = say + str(count) + str(last_c)
           last_c = c
           count = 1
    say = say + str(count) + str(last_c)
    return say

s='1'
#print s, 1, 0
for i in range(1,6):
    s = lookNsay(s)
    print s #, i, len(s)

#print len(s)

import re
 
for m in re.finditer(r"(\d)\1*", s):
    print m.group(0), m.group(1)


print '====================='
s = '1111aa12345aa111232211aa2'

for m in re.finditer(r"([0-9])\1*", s):
    print m.group(0), m.group(1)



'''
import re
def describe(s):
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(30):
    s = describe(s)
print len(s)  # prints 5808
'''
