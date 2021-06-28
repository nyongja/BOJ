n = int(input())
answer = 0
for i in range(1, n) :
    s_num = str(i)
    n_sum = i

    for j in s_num :
        n_sum += int(j)
    if n_sum == n :
        answer = i
        break

print(answer)