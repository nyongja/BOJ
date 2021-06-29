from itertools import product

n, m = map(int, input().split())

array = [i for i in range(1, n + 1)]
array = product(array, repeat = m)

for i in array :
    for j in range(m) :
        print(i[j], end = ' ')
    print()