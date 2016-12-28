#!/usr/bin/env python
import os
import urllib
import urllib2
import base64
import xmlrpclib
import datetime
import re, Image

url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
base64string = base64.encodestring('%s:%s' % ('huge', 'file'))[:-1]
req = urllib2.Request(url)
req.add_header("Authorization", "Basic %s" % base64string)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page


import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.system.listMethods()
print proxy.system.methodHelp('phone')
print proxy.phone('Bert')
print proxy.phone('555-ITALY')




import thread
import time
import datetime
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def ServerThreadfun(string, sleeptime, *args):
    def today(x):
        print x
        today = datetime.datetime.today()
        return xmlrpclib.DateTime(today)

    server = SimpleXMLRPCServer(("localhost", 8000))
    print "Listening on port 8000..."
    server.register_introspection_functions()
    server.register_function(today, "today")
    server.serve_forever()



thread.start_new_thread(ServerThreadfun, ("ThreadFun", 1))

time.sleep(1)

proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
print proxy.system.listMethods()

today = proxy.today('2234')
# convert the ISO8601 string to a datetime object
converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
print "Today: %s" % converted.strftime("%d.%m.%Y, %H:%M")


