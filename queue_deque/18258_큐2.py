from sys import stdin


class Queue :
    def __init__(self) :
        self.queue = list()
        self.top = 0
        self.rear = -1

    def push(self, x) :
        self.queue.append(x)
        self.rear += 1
    
    def pop(self) :
        if self.empty() :
            return -1
        else :
            self.top += 1
            return self.queue[self.top - 1]

    def size(self) :
        return self.rear - self.top + 1

    def empty(self) :
        if self.top - self.rear == 1:
            return 1
        else :
            return 0

    def front(self) :
        if self.empty() :
            return -1
        else :
            return self.queue[self.top]
    
    def back(self) :
        if self.empty() :
            return -1
        else :
            return self.queue[self.rear]

n = int(stdin.readline())
queue = Queue()

for _ in range(n) :
    command = stdin.readline().split()
    if command[0] == 'push' :
        queue.push(command[1])
    elif command[0] == 'pop' :
        print(queue.pop())
    elif command[0] == 'size' :
        print(queue.size())
    elif command[0] == 'empty' :
        print(queue.empty())
    elif command[0] == 'front' :
        print(queue.front())
    elif command[0] == 'back' :
        print(queue.back())
    