#!/usr/bin/env python
import os
import urllib
import urllib2
import base64

url = 'http://www.pythonchallenge.com/pc/return/good.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

first_idx = the_page.rfind("first:") + 7
second_idx = the_page.rfind("second:") + 8
end_idx = the_page.rfind("-->")


first = the_page[first_idx:second_idx-8];
second = the_page[second_idx:end_idx];

print first
print second

first = first.replace('\n','').split(',')
second = second.replace('\n','').split(',')
print first
print second


first = [int(x) for x in first]
second = [int(x) for x in second]
print first,len(first)
print second,len(second)


import turtle

turtle.reset()
turtle.setworldcoordinates( 0, 500, 500, 0)

turtle.penup()
turtle.pensize(1)
turtle.setposition( first[0], first[1] )
turtle.pendown()
for x in range( 0, len(first), 2):
    turtle.setposition( first[x], first[x+1] )


turtle.penup()
turtle.pensize(2)
turtle.setposition( second[0], second[1] )
turtle.pendown()
for x in range( 0, len(second), 2):
    turtle.setposition( second[x], second[x+1] )



input()




