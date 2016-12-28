#!/usr/bin/env python

import string


#abcdefghijklmnopqrstuvwxyz
#  abcdefghijklmnopqrstuvwxyz           

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

ar = bytearray(s)
i = 0
for d in ar:
    if d == ord('y'): 
        ar[i] = 'a'
    elif d == ord('z'):
        ar[i] = 'b' 
    elif d >= ord('a') and d <= ord('x'):
        ar[i] = d + 2;
    i = i + 1
        
print(ar)


# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


from string import maketrans   

intab = "abcdefghijklmnopqrstuvwxyz"
outtab ="cdefghijklmnopqrstuvwxyzab"

trantab = maketrans(intab, outtab)

url = "http://www.pythonchallenge.com/pc/def/map.html"
print url.translate(trantab)

#http://www.pythonchallenge.com/pc/def/ocr.html


