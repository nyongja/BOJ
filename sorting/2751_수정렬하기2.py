import sys

ipt = sys.stdin.readline
array = []

for _ in range(int(ipt())) :
    array.append(int(ipt()))
array.sort()

for i in array :
    print(i)