import math
import random
def permutation(n):
    global c
    c=[]
    while len(c)<math.factorial(n):
        a=list(range(1,n+1))
        b=[]
        while len(b)<n:
            e= a[random.randint(0,n-1)]
            if e not in b:
                b.append(e)
        if b not in c:
            c.append(b)
        b=[]

if __name__ == '__main__':
    n=4
    permutation(n)
    print(c)





