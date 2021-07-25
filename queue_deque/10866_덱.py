from sys import stdin

class Deque :
    def __init__(self) :
        self.queue1 = list()
        self.queue2 = list()

    def push_front(self, x) :
        self.queue2.append(x)

    def push_back(self, x) :
        self.queue1.append(x)
    
    def pop_front(self) :
        if self.size() == 0 :
            return -1
        elif self.empty(self.queue2) == 0:
            return self.queue2.pop()
        else :
            while self.empty(self.queue1) == 0:
                self.queue2.append(self.queue1.pop())

        return self.queue2.pop()

    def pop_back(self) :
        if self.size() == 0 :
            return -1
        elif self.empty(self.queue1) == 0:
            return self.queue1.pop()
        else :
            while self.empty(self.queue2) == 0:
                self.queue1.append(self.queue2.pop())

        return self.queue1.pop()

    def size(self) :
        return len(self.queue1) + len(self.queue2)

    def empty(self, queue) :
        if queue == 'all' :
            if self.size() == 0 :
                return 1
            return 0
        elif len(queue) == 0 :
            return 1
        return 0

    def front(self) :
        if self.size() == 0 :
            return -1
        elif self.empty(self.queue2) :
            return self.queue1[0]
        else :
            return self.queue2[-1]
    
    def back(self) :
        if self.size() == 0 :
            return -1
        elif self.empty(self.queue1) :
            return self.queue2[0]
        else :
            return self.queue1[-1]

deque = Deque()
n = int(input())
for _ in range(n) :
    command = stdin.readline().split()
    if command[0] == 'push_front' :
        deque.push_front(command[1])
    elif command[0] == 'push_back' :
        deque.push_back(command[1])
    elif command[0] == 'pop_front' :
        print(deque.pop_front())
    elif command[0] == 'pop_back' :
        print(deque.pop_back())
    elif command[0] == 'size' :
        print(deque.size())
    elif command[0] == 'empty' :
        print(deque.empty('all'))
    elif command[0] == 'front' :
        print(deque.front())
    elif command[0] == 'back' :
        print(deque.back())

 