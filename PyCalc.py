#!/bin/python3

# Terminal based calculator
#############################
# Version 0.1
# 2017.06.13

def doMath(x, y, act):
  if(act=="+"):
    return x+y

  


x = int(input("insert first number and press ENTER..."))
act=input("enter operation + - * /")
y = int(input("insert second number and press ENTER..."))
print(doMath(y, x, act))

