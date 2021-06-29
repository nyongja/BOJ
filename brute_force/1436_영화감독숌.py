n = int(input())

num = 665
pattern = '666'

while n > 0 :
    num += 1
    if pattern in str(num) :
        n -= 1
print(num)