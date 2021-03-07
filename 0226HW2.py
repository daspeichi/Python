#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 22:20:55 2021

@author: ElishaYi
"""

for i in range(10,1,-1):
    for a in range (1,i):
        print(a,end='')
    print()

"""
i => [10,9,8,7,6,5,4,3,2]
a => (1,10) => 123456789
  => (1,9) => 12345678
     .
     .
     .
  =>(1,3) => 12
  =>(1,2) => 1
"""

