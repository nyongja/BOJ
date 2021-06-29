import sys
ipt = sys.stdin.readline

n = int(ipt())
array = []
for _ in range(n) :
    age, name = map(str, ipt().split())
    age = int(age)
    array.append((age, name))

array = sorted(array, key = lambda x : x[0])

for age, name in array :
    print(age, name)