expression = input()

flag = False # -가 등장하면 모든 수 빼주면 됨(괄호로 묶어준다고 생각)
num = ''
answer = 0

for i in expression :
    if i == '+' and flag == False : # - 등장 전
        answer += int(num) # 무조건 더해주기
        num = ''
    elif i == '-' and flag == False : # - 첫 번째 등장
        answer += int(num) # 그전 까지는 더해주기
        num = ''
        flag = True
    elif (i == '-' or i == '+') and flag == True : # - 등장 이후
        answer -= int(num) # 무조건 빼주기
        num = ''
    else :
        num += i
        
# 마지막 숫자 계산
if flag :
    answer -= int(num)
else :
    answer += int(num)

print(answer)