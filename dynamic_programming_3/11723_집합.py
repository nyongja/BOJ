import sys
input =sys.stdin.readline
m = int(input()) # 수행해야하는 연산 수
s = set()

bit = 0
for _ in range(m) :
    commands = input().split() # 명령어, 숫자

    if commands[0] == "all" :
        bit = (1 << 20) -1
    elif commands[0] == "empty" :
        bit = 0
    else :
        op = commands[0]
        num = int(commands[1])-1

        if op == "add" :
            bit |= (1<<num)
        elif op == "remove" :
            bit &= ~(1<<num)
        elif op == "check" :
            if bit & (1<<num) == 0 :
                print(0)
            else :
                print(1)
        elif op == "toggle" :
            bit ^= (1<<num)