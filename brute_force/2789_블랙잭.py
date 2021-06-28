n, m = map(int, input().split())
card = list(map(int, input().split()))

answer = 0

for i in range(0, n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            tmp = card[i] + card[j] + card[k]
            if tmp > answer and tmp <= m :
                answer = tmp

print(answer)