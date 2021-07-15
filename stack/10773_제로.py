k = int(input())

stack = list()
for _ in range(k) :
    n = int(input())
    if n == 0 :
        stack.pop()
    else :
        stack.append(n)

answer = 0
for i in stack :
    answer += i

print(answer)