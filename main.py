import pandas as pd
from random import randint

n = int(input('2부터 6 사이의 정수를 입력하세요: '))
main_list = [[randint(1, 100) for j in range(n)] for i in range(n)]
df = pd.DataFrame(main_list,
    columns=["작업" + str(i + 1) for i in range(n)],
    index=["기계" + chr(65 + i) for i in range(n)])
print(df)
print('esther')