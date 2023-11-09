n,m = map(int,input().split())
board = [] #전체 보드
result = [] 
for _ in range(n):
    board.append(input())
    
for i in range(n-7): #8x8을 검사하므로 전체 보드판의 인덱스를 벗어나면 안됨
    for j in range(m-7):
        draw1 = 0 #시작점이 W인 경우, B인 경우를 나눠서 검사
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'B':
                        draw1 +=1
                    if board[a][b] != 'W':
                        draw2 +=1
                else:
                    if board[a][b] != 'W':
                        draw1 +=1
                    if board[a][b] != 'B':
                        draw2 +=1
        result.append(draw1)
        result.append(draw2)
print(min(result)) #결과값 중 최솟값 출력