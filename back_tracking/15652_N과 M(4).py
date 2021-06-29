from itertools import combinations_with_replacement

n, m = map(int, input().split())

array = [i for i in range(1, n + 1)]
array = list(combinations_with_replacement(array, m))

for i in array :
    for j in range(m) :
        print(i[j], end = ' ')
    print()