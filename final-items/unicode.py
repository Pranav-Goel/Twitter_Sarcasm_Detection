

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
__author__ = 'PRAYAS2'
f= open('Unique-tweets-sarc-comb2.txt20160311-215402 - Copy.txt')
f.seek(0)
for t in f.readlines() :
    print(t)




