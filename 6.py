#!/usr/bin/env python

import urllib
import pickle
import zipfile, os

from shutil import copyfile


#content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/channel.html").read()
#print content


#content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/zip.html").read()
#print content


#copyfile( os.path.join(os.getcwd(), 'channel.zip'), os.path.join(os.getcwd(), 'channel_tmp.zip'))
zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), 'channel.zip'))

ziplist = zipFile.namelist()


def next_zip(next_string, count, comments):

    print next_string 

    fname = next_string+".txt"
    content = zipFile.read(fname)

    zipInfo = zipFile.getinfo(fname)
    comment = zipInfo.comment
    #print 'comment:', comment

    ziplist.remove(fname)
    #print content,

    index = content.rfind("is")
    #print index
    if index > 0:
       next = content[3+index:]
       #print next       
       x, s = next_zip(next, count, comments)
       return x+1, comment+s
    else:
	zipInfo = zipFile.getinfo(fname)
	return count + 1, comment


count, string = next_zip("90052", 0, "")
print string
print count

#for f in ziplist:
#    print f



zipFile.close()



content = urllib.urlopen("http://www.pythonchallenge.com/pc/def/hockey.html").read()
print content






#import zipfile, re
#findnothing = re.compile(r"Next nothing is (\d+)").match
#comments = []
#z = zipfile.ZipFile("channel.zip", "r")
#seed = "90052"
#while True:
#    fname = seed + ".txt"
#    comments.append(z.getinfo(fname).comment)
#    guts = z.read(fname)
#    m = findnothing(guts)
#    if m:
#        seed = m.group(1)
#    else:
#        break
#print "".join(comments)
