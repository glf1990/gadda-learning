#!/usr/bin/python3

def power(x):
    return x*x 

def power1(x,n=2): 
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

if __name__=="__main__":
    print("f1\n")
    print(power(3))
    print(power1(3))

    print(power1(3,n=4))
    print(power1(3))
