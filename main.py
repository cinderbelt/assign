import pandas as pd
from random import randint
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

n = int(input('2부터 6 사이의 정수를 입력하세요: '))
main_list = [[randint(1, 100) for j in range(n)] for i in range(n)]
df = pd.DataFrame(main_list,
                  columns=["작업" + str(i + 1) for i in range(n)],
                  index=["기계" + chr(65 + i) for i in range(n)])
print(df)
permutation(n)
permutation_list=c
sum=0
sum_list=[]
for j in range(len(permutation_list)):
    for i in range(n):
        sum+=int(df.iloc[i,permutation_list[j][i]-1])
    sum_list.append(sum)
    sum=0

print(permutation_list)
print(sum_list)
min= min(sum_list)
print(min)
print(sum_list.index(min))
print(permutation_list[sum_list.index(min)])