#!/usr/bin/env python

import urllib

#content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

#print content

"""
end = content.rfind( "-->")
print end

start = content.rfind( "<!--")
print start

book = content[start:end];

print book

for c in book:
    if c >= 'a' and c <= 'z':
        print c,
    elif c >= 'A' and c <= 'Z':
        print c,
    elif c >= '0' and c <= '9':
        print c,


print " "


s = ''.join([line.rstrip() for line in content])    
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = len(s) // len(OCCURRENCES)
print ''.join([c for c in s if OCCURRENCES[c] < avgOC])   

"""

content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

end = content.rfind( "-->")
start = content.rfind( "<!--")

data = content[start:end];

letters = "abcdefghijklmnopqrstuvwxyz"
letterl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


big_count=0
small_c = 0
state = 0

# state = 0  get big:   if big_count==3 =>state 1
#            get small: =>state 0
#
# state = 1  get big:   state=>0
#            get small: small_c = c, big_count=0, =>state 2
#
# state = 2  get big:   if big_count==3 =>state 3
#            get small: =>state 0
#
# state = 3  get big:   =>state 0
#            get small: print, =>state 0


for c in data:    
    if c >= 'a' and c <= 'z':
        big_count = 0
	if state == 0:
           state = 0
        elif state == 1:
           small_c = c
           state = 2
        elif state == 2:   
           state = 0
        elif state == 3: 
           print small_c, 
           state = 0

    if c >= 'A' and c <= 'Z':
        big_count = big_count + 1 
	if state == 0:           
           if big_count == 3:
              state = 1
        elif state == 1: 
           state = 0
        elif state == 2: 
           if big_count == 3:
              state = 3
        elif state == 3: 
           state = 0

