#!/usr/bin/env python

import urllib

content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

#print content

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



content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

end = content.rfind( "-->")
start = content.rfind( "<!--")
guts = content[start:end];

d = {}
for ch in guts:
    d[ch] = d.get(ch, 0) + 1
print "".join(ch for ch in guts if d[ch] == 1)  # requires Python 2.4




