#!/usr/bin/env python
import os
import urllib
import png
import numpy


content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.html").read()
print content


#png=png.Reader(urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")).read()
#print png

from PIL import Image
im = Image.open( os.path.join(os.getcwd(),'oxygen.png') )
ll = list(im.getdata())

s=""
c=0
for pixel in ll:
    if c!=pixel[0] and pixel[0] == pixel[1] == pixel[2]:
       #print pixel
       c = pixel[1]
       s = s + chr(c)

print s     

#[105, 10, 16, 101, 103, 14, 105, 16, 121] 
#[105, 110, 116, 101, 103, 114, 105, 116, 121]

#print im.info
#im.rotate(45).show()
#im.show()



import re, Image

i = Image.open("oxygen.png") # http://www.pythonchallenge.com/pc/def/oxygen.png
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

#print row
print "".join(map(chr, ords))
#print ords

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))
