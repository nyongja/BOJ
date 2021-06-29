import sys

ipt = sys.stdin.readline
array = [0] * 10001
n = int(ipt())

# Counting Sort
for _ in range(n) :
    num = int(ipt())
    array[num] += 1

for i in range(10001) :
    if array[i] != 0 :
        for _ in range(array[i]) :
            print(i)