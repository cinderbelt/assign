import pandas as pd
from random import randint
import permuting as pm

n = int(input('2부터 6 사이의 정수를 입력하세요: '))
main_list = [[randint(1, 100) for j in range(n)] for i in range(n)]
df = pd.DataFrame(main_list,
                  columns=["작업" + str(i + 1) for i in range(n)],
                  index=["기계" + chr(65 + i) for i in range(n)])
print(df)
pm.permutation(n)
permutation_list=pm.c
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