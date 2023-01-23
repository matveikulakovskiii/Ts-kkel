from math import *
from random import *

try:
    a=int(input("Mitu kuud aastas? ->"))
    while True:
        if a!=12:
            print("veidi üle poole")
            a=int(input("Mitu kuud aastas? ->"))
        else:
            print("Õige vastus")
            break
except:
    print("Vale Andmed")



try:
    for i in range(1,100,1):
        s=int(input("Mitu kuud aastas? ->"))
        if s==12:
            print("Õige vastus")
            break
        else:
            print("Vale vastus")
except:
    print("Vale Andmed")



#x=1
#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end=" ")


#a=random.randint(1,100)
#b=0
#while b!= a:
#    try:
#        b=int(input("sisesta arv vahemikus 1-100: "))
#        if b>100 and b<1:
#            print("Vahemik on vale")
#        if b<a:
#            print("Liiga väike! Proovi uuesti.")
#        elif b>a:
#            print("Liiga suur! Proovi uuesti.")
#        else:
#            print("Palju õnne! Sa arvaksid mõistatuslik numbri ära.", a)
#            break
#    except:
#        print("Value Error")

try:
    numbers = input("Sisestage mitu komadega eraldatud numbrit: ").split(",")
    sum = 0
    product = 1
    count = 0

    for number in numbers:
        number = float(number)
        sum += number
        product *= number
        count += 1

    arithmetic_mean = sum/count
    geometric_mean = pow(product, 1/count)

    print("summa:", sum)
    print("aritmeetiline keskmine:", arithmetic_mean)
    print("geomeetriline keskmine:", geometric_mean)
    print("korrutis:", product)
except:
    print("Vale Andmed")
