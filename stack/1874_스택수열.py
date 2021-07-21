n = int(input())
stack = list()
answer = list()
tmp_n = 1 # 스택에 마지막으로 들어간 숫자
flag = True

for _ in range(n) :
    num = int(input())
    while tmp_n <= num : # 만약 다음에 나와야 할 숫자까지 스택에 들어가있지 않으면
        stack.append(tmp_n) # 일단 넣기
        tmp_n += 1
        answer.append('+')
    if tmp_n == num : # 마지막으로 들어간 숫자가 내가 원하는 숫자랑 같으면
        stack.pop() # 뽑기
        answer.append('-')
    elif tmp_n > num : # 마지막으로 들어간 숫자가 내가 원하는 숫자보다 크면
        if stack.pop() != num : # 뽑아서 내가 원하는 숫자가 있는지 비교해보기
            flag = False 
            break
        else :     
            answer.append('-')

if flag :
    print(*answer)
else :
    print("NO")