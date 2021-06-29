import sys
ipt = sys.stdin.readline

num = list(str(int(ipt())))
array = [0] * 10

# 자릿수에 들어갈 수 있는 숫자는 0 ~ 9 이므로 counting sort
for i in num :
    array[int(i)] += 1

for i in range(10) :
    idx = 9 - i
    if array[idx] != 0 :
        for _ in range(array[idx]) :
            print(idx, end = '')