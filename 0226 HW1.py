#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:51:19 2021

@author: ElishaYi
"""


for i in range(1,5):
    for a in range(1,i+1):
        print(a,end='')
    print()
print("Finish")


'''
for i in range(1,3):
    for a in range(1,i+1):
        print(a,end='')
    print()
print("Finish")

# i => [1,2]
  a => (1,1+1) => (1,2) => 1 (終止值不算)
    => (1,2+1) => (1,3) => 12 
'''
