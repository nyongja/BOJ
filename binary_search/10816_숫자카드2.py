from collections import defaultdict

n = int(input())
card = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
card.sort()
count = defaultdict(int)

def binary_search(start, end, target) :
    while start <= end :
        mid = (start + end) // 2
        if card[mid] > target :
            end = mid - 1
        elif card[mid] < target :
            start = mid + 1
        elif card[mid] == target :
            return 1
    return 0

for i in card :
    count[i] += 1

answer = list()
for i in targets :
    tmp = binary_search(0, len(card)-1, i)
    if tmp == -1 :
        answer.append(0)
    else :
        answer.append(count[i])
print(*answer)