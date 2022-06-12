# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:20:29 2022

@author: Yuxinz
"""
data=""
with open('raw/20220419.txt','r',encoding='utf-8') as f:
    text=f.readline()
    if text[0]=='C':
        text=f.readline()
    while text:
        text=list(text)
        del text[0:3]
        del text[-2:-1]
        text="".join(text)
        data+=text
        text=f.readline()
with open('processed/20220419.txt',"w",encoding="utf-8") as f:
    f.write(data)
    
 