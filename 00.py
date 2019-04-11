# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:20:30 2019

@author: 76947
"""
import numpy
class Line:
    def __init__(self,c0,c1):
        self.c0=c0
        self.c1=c1
    def __call__(self,x):
        return self.c0+self.c1*x
    def table(self,L,R,n):
        s=''
        for x in numpy.linspace(L,R,n):
            y=self(x)
            s+='%12g %12g\n'%(x,y)
        return s
class P(Line):
    def __init__(self,c0,c1,c2):
        Line.__init__(self,c0,c1)
        self.c2=c2
    def __call__(self,x):
        return Line.__call__(self,x)
p=P(-1,-2,2)
l=Line(-1,-2)
print(isinstance(l,P))
print(isinstance(p,Line))



        
