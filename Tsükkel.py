from math import *
from random import *

#try:
#    a=int(input("Mitu kuud aastas? ->"))
#    while True:
#        if a!=12:
#            print("veidi üle poole")
#            a=int(input("Mitu kuud aastas? ->"))
#        else:
#            print("Õige vastus")
#            break
#except:
#    print("Vale Andmed")



#try:
#    a=int(input("Mitu kuud aastas? ->"))
#    while a<12:
#        if a==12:
#            print("Õige vastus")
#        else:
#            a=int(input("Mitu kuud aastas? ->"))
#except:
#    print("Vale Andmed")



#try:
#    for i in range(1,100,1):
#        s=int(input("Mitu kuud aastas? ->"))
#        if s==12:
#            print("Õige vastus")
#            break
#        else:
#            print("Vale vastus")
#except:
#    print("Vale Andmed")



#x=1
#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end=" ")


a=random.randint(1,100)
b=0
while b!= a:
    try:
        b=int(input("sisesta arv vahemikus 1-100: "))
        if b>100 and b<1:
            print("Vahemik on vale")
        if b<a:
            print("Liiga väike! Proovi uuesti.")
        elif b>a:
            print("Liiga suur! Proovi uuesti.")
        else:
            print("Palju õnne! Sa arvaksid mõistatuslik numbri ära.", a)
            break
    except:
        print("Value Error")