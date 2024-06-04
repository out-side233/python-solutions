#!/usr/bin/env python


def mark(s):
    res=[]
    #check redundant ')'
    flag=0
    for i in s:
        if i =='(':
            flag+=1
            res.append(' ')
        elif i==')':
            if flag>0:
                flag-=1
                res.append(' ')
            else: res.append('?')
        else:res.append(' ')
    #check for '('
    s1=s[::-1]
    flag1=0
    for i in range(len(s1)):
        if s1[i]==')':
            flag1+=1       
        elif s1[i]=='(':
            if flag1>0:
                flag1-=1
            else: res[len(s1)-i-1]=('x')
    res=''.join(res)
    return res
    

s=[
'bge)))))))))',
'((IIII))))))',
'()()()()(uuu',
'))))UUUU((()']


for c in s:
    print(c)
    print(mark(c))

