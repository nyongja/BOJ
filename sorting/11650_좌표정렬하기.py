import sys
ipt = sys.stdin.readline

n = int(ipt())
array = []
for _ in range(n) :
    x, y = map(int, ipt().split())
    array.append((x, y))

array = sorted(array, key = lambda x : (x[0], x[1]))

for x, y in array :
    print(x, y)   
