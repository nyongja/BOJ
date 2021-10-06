import sys
input = sys.stdin.readline
from copy import deepcopy
'''
            U(w)
          0  1  2
          3  4  5
          6  7  8
L(g)     __________    R (b)           B(o)
36 37 38|F18 19 20 | 45 46 47 | 27 28 29
39 40 41|r21 22 23 | 48 49 50 | 30 31 32
42 43 44| 24 25 26 | 51 52 53 | 33 34 35
        -----------
          9  10 11
          12 13 14
          15 16 17
          D(y)
'''
to_color = {0 : 'w', 1 : 'y', 2 : 'r', 3 : 'o', 4 : 'g', 5 : 'b'}
rot = [[36,37,38,18,19,20,45,46,47,27,28,29], # U
       [33,34,35,51,52,53,24,25,26,42,43,44], # D
       [6,7,8,44,41,38,11,10,9,45,48,51], # F
       [2,1,0,53,50,47,15,16,17,36,39,42], # B
       [0,3,6,35,32,29,9,12,15,18,21,24], # L
       [8,5,2,26,23,20,17,14,11,27,30,33] # R
]
inner_rot = [0, 1, 6, 3, 8, 7, 2, 5]

def cube_init() :
    cube = [0] * 54
    for i in range(6) :
        for j in range(9) :
            cube[i*9 + j] = to_color[i]
    return cube

def rotate(a, b) :
    b = to_integer[b]
    a = to_integer[a]
    outer_rotate(a, b)
    inner_rotate(a, b)


def outer_rotate(a, b) :
    global cube
    tmp_cube = deepcopy(cube)
    cur_rot = rot[a]
    for i in range(len(cur_rot)) :
        tmp_cube[cur_rot[i]] = cube[cur_rot[(i+b*3) % 12]]
    cube = deepcopy(tmp_cube)

def inner_rotate(a, b) :
    global cube
    tmp_cube = deepcopy(cube[a*9:a*9+9])
    print("tmp_cube : ", tmp_cube)
    print("inner rot : ", inner_rot)
    for i in range(8) :
        print(inner_rot[i], inner_rot[(i+b*2) % 8], tmp_cube[inner_rot[i]], cube[a*9 + inner_rot[(i+b*2)%8]])
        tmp_cube[inner_rot[i]] = cube[a*9 + inner_rot[(i+b*2)%8]]
    cube[a*9:a*9+9] = deepcopy(tmp_cube)

def print_cube() :
    for j in range(3) :
        for k in range(3) :
            print(cube[j*3+k], end = '')
        print('')
    
def print_all() :
    for i in range(6) :
        for j in range(3) :
            for k in range(3) :
                print(cube[i*9 + j*3 + k], end = '')
            print('')
        print('')

to_integer = {'U' : 0, 'D' : 1, 'F' : 2, 'B' : 3, 'L' : 4, 'R' : 5, '+' : 1, '-' : 3}
t = int(input()) # 테스트 케이스 수
a, b = 0, 0
for _ in range(t) : 
    cube = cube_init()
    print_all()
    print(")))!(((@)")
    n = int(input()) # 큐브 돌린 횟수
    move = list(map(str, input().split()))
    for i in move :
        a, b = i.strip()
        rotate(a, b)
        print_all()
        print('-----------------')
    print_cube()