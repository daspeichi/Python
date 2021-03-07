#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:40:26 2021

@author: ElishaYi
"""

#輸入迴圈次數，判斷哪些數值是奇數，哪些是偶數
#用一個for迴圈完成，for迴圈中用if...else

number = int(input("請輸入數字："))
even=[]
odd=[]
for i in range (1,number+1):
    if i%2 ==0:
        even=even+[i]
        
    else:
        odd=odd+[i]
print("偶數總和：",even)
print("奇數總和：",even)