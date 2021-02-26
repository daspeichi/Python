# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:48:15 2021

@author: USER
"""
#輸入迴圈次數，判斷哪些數值是奇數，哪些是偶數

number = int(input("請輸入次數："))
for i in range (1,number+1):
    if i%2 ==0:
        print (i)
print("上列數字為偶數")

for i in range (1,number+1):
     if i%2 !=0:
        print (i)
print("上列數字為奇數")
    
print ("程式執行完畢")