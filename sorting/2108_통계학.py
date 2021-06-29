from collections import Counter
import sys

ipt = sys.stdin.readline

n = int(ipt())
array = []

for _ in range(n) :
    array.append(int(ipt()))

array = sorted(array)

if n == 1 :
    print(array[0])
    print(array[0])
    print(array[0])
    print(0)

else :
    # 1. 산술 평균
    mean = round(sum(array) / len(array))
    print(mean)

    # 2. 중앙값
    median = array[int(len(array)/2)]
    print(median)

    # 3. 최빈값
    cnt = Counter(array)
    mode = cnt.most_common()
    mode = sorted(mode, reverse = True, key = lambda x : x[1])

    if mode[0][1] == mode[1][1] :
        print(mode[1][0])
    else :
        print(mode[0][0])

    # 4 . 범위
    range = array[-1] - array[0]
    print(range)