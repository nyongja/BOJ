n = int(input())
array = list(map(int, input().split()))
max_n = -1 * int(1e9)

for i in range(len(array)) :
    if i == 0 : # 초기값 
        tmp = array[0] # 더해가면서 값 확인 
        prev = array[0] # 이전 값
    else :
        tmp += array[i] # 계속 더해주기

    max_n = max(max_n, prev) # 최댓값 확인
    prev = tmp
    
    if i == n-1 : # 마지막 값의 경우 현재 값도 한 번 확인
        max_n = max(max_n, tmp)

    if tmp < 0 : # tmp가 0보다 작으면 계속 더하는게 의미가 없으므로 처음부터 다시 더하기
        tmp = 0

print(max_n)