string = input()
while string != "." :
    stack = list()
    flag = True
    for i in string :
        if i == "(" or i == "[" :
            stack.append(i)
        elif i == ")" or i == "]" :
            if stack :
                prev = stack.pop()
                if (i == ")" and prev != "(") or (i == "]" and prev != "[") : # 짝이 안맞으면
                    flag = False
                    break
            else : # 스택이 비어있으면
                flag = False
                break

    if flag and stack : # 짝은 맞았는데 아직 스택에 괄호가 남아있으면
        flag = False
    if flag :
        print("yes")
    else :
        print("no")
    string = input()
