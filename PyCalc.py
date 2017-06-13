#!/bin/python3

# Terminal based calculator
#############################
# Version 0.1
# 2017.06.13

def doMath(x, y, act):
  if(act=="+"):
    return x+y
  elif(act=="-"):
    return (x-y)
  elif(act=="*"):
    return x*y
  elif(act=="/"):
    result = 0
    try:
      result = x/y
    except ZeroDivisionError:
      print("Nelze dělit nulou!")
      exit()
    return result 
  


x = int(input("insert first number and press ENTER..."))
act=input("enter operation + - * /:  ")
y = int(input("insert second number and press ENTER..."))
print(doMath(x, y, act))

