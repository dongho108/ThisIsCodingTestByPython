def displaysnake(snake, n):
    print(snake)
    temp = [[0]*(len(board)) for i in range(n)]
    for i in range(len(snake)):
        temp[snake[i][0]][snake[i][1]] = 1
    for i in range(1, n):
        for j in range(1, n):
            print(temp[i][j], end=' ')
        print()


n = int(input())
k = int(input())
board = [[0]*(n+1) for i in range(n+1)]

for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 2

l = int(input())
dirlist = [[0, 'X'] for i in range(l)]
for i in range(l):
    x, y = input().split()
    dirlist[i] = [x, y]

snake = [[1, 1]]
snakeDir = 1 # 0:북 1:동 2:남 3:서
board[1][1] = 1
time = 0
snakeTime = 0

go = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0


while True:
    nextX = snake[0][0]+go[snakeDir][0]
    nextY = snake[0][1]+go[snakeDir][1]
    count += 1
    if nextX < 1 or nextX > n or nextY < 1 or nextY > n\
            or board[nextX][nextY] == 1:
        break
    snake.insert(0, [nextX, nextY])

    if board[nextX][nextY] == 2:
        pass
    else:
        a, b = snake.pop()
        board[a][b] = 0
        pass
    # displaysnake(snake, len(board))
    board[nextX][nextY] = 1
    time += 1

    if snakeTime == len(dirlist):
        continue
    if time == int(dirlist[snakeTime][0]):
        if dirlist[snakeTime][1] == 'D':
            snakeDir = (snakeDir+1) % 4
        else:
            snakeDir = (snakeDir+3) % 4
        snakeTime += 1


print(count)
