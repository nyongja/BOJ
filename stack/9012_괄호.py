t = int(input())

for _ in range(t) :
    ps = input()
    stack = list()
    flag = True
    for i in ps :
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if len(stack) == 0 :
                flag = False
                break
            else :
                stack.pop()
    if flag :
        if len(stack) != 0 :
            flag = False
    
    if flag :
        print("YES")
    else :
        print("NO")
