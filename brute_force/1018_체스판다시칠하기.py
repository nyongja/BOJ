n, m = map(int, input().split())
chess = []
for _ in range(n) :
    chess.append(list(input()))

answer = int(1e9)

for row in range(n - 7) :
    for col in range(m - 7) :
        slice_chess = [chess_row[col:col+8] for chess_row in chess[row:row+8]]
        cntB = 0
        cntW = 0
        for i in range(8) :
            for j in range(8) :
                if i % 2 == 0 and j % 2 == 0 : 
                    if slice_chess[i][j] != 'B' : 
                        cntB += 1
                    else :
                        cntW += 1
                elif i % 2 == 0 and j % 2 == 1 :
                    if slice_chess[i][j] != 'W' : 
                        cntB += 1
                    else :
                        cntW += 1
                elif i % 2 == 1 and j % 2 == 0 :
                    if slice_chess[i][j] != 'W' : 
                        cntB += 1
                    else :
                        cntW += 1
                elif i % 2 == 1 and j % 2 == 1 :
                    if slice_chess[i][j] != 'B' : 
                        cntB += 1
                    else :
                        cntW += 1 
        cntMin = min(cntB, cntW)
        answer = min(cntMin, answer)
print(answer)
            
