# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 17:31:28 2023

@author: lidor
"""

def my_func(x1,x2,x3):
    if type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
    elif type(x1) != float or type(x2) != float or type(x3) != float :
         return (print(None))
    elif (x1+x2+x3) == 0:
        print("Not a number – denominator equals zero")
    else:
        Result = float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
        return(print(Result))

my_func(1.0,1.0,1.0)


