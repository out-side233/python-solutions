#!/usr/bin/env python
# coding: utf-8


def check(source,target):
    s=set(source)
    if any (c not in s for c in target):
        return -1
    res,i=0,0
    for c in target:
        while i<len(source)-1 and c!=source[i]:
            i+=1
        if i==len(source)-1:
            res+=1
            i=0
        elif source[i]==c:
            i+=1
    return res
            


a=['abc','abc','xyz']
b=['abcbc','acdbc','xzyxz']
for x,y in zip(a,b):
    print(check(x,y))


