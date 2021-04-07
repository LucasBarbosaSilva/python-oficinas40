import math

def dividers(num, cont):
    if (num >= cont):
        if(num % cont == 0):
            
            print("%d" %cont)
        dividers(num, cont + 1)

def multiple(num):
    print (num * 1, ',', num * 2, 'e', num * 3)

def isInterger(num):
    raiz = math.sqrt(num)
    
    print ("Esse número %s tem raiz inteira" %(raiz % 1 == 0 if "" else "não") )

dividers(40, 1)
multiple(40)
isInterger(40)