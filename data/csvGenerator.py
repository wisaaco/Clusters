# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:34:39 2017

@author: isaac
"""
import random
#import sys
import string

#registros = sys.argv[1]
registros = 10000000
f = open("movies_out.csv","w")

for i in range(1,registros+1):
   year = random.randint(1900, 2016)
   ran = random.uniform(1,5)
   mil = random.randint(2000, 8000)
   name = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
   f.write("%i,%s,%i,%0.1f,%i\n" %(i,name,year,ran,mil))

f.close()
print "Done"