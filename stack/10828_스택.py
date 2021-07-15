from sys import stdin

class Stack :
    def __init__(self) :
        self.stack = list()
    
    def push(self, x) :
        self.stack.append(x)
        
    def pop(self) :
        if self.empty() :
            return -1
        return self.stack.pop()
    
    def size(self) :
        return len(self.stack)

    def empty(self) :
        if self.size() == 0 :
            return 1
        return 0
    
    def top(self) :
        if self.empty() :
            return -1 
        return self.stack[self.size()-1]

stack = Stack()

n = int(stdin.readline())
for _ in range(n) :
    input_lst = stdin.readline().split()
    command = input_lst[0]
    if command == 'push' :
        stack.push(int(input_lst[1]))
    elif command == 'pop' :
        print(stack.pop())
    elif command == 'size' :
        print(stack.size())
    elif command == 'empty' :
        print(stack.empty())
    elif command == 'top' :
        print(stack.top())