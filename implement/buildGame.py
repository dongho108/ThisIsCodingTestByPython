n, m = map(int, input().split())
x, y, currentDir = map(int, input().split())
gameMap = [[0]*m for i in range(n)]

for i in range(n):
    gameMap[i] = list(map(int, input().split()))

dirList = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def checkleft(x, y, dir): # 왼쪽이 가봤거나 바다인지 체크
    leftdir = (dir+3) % 4
    if gameMap[x + dirList[leftdir][0]][y + dirList[leftdir][1]] > 0:
        return False
    else:
        return True


def rotationleft(dir):  # 왼쪽으로 회전
    return (dir+3) % 4


def go(x, y, dir):  # 현재 방향으로 앞으로 감
    x = x + dirList[dir][0]
    y = y + dirList[dir][1]
    return x, y


def checkback(x, y, dir):  # 뒤쪽이 바다인지 체크
    leftdir = (dir + 2) % 4
    if gameMap[x + dirList[leftdir][0]][y + dirList[leftdir][1]] == 1:
        return False
    else:
        return True


def back(x, y, dir): # 현재 방향에서 뒤로 감
    backdir = (dir+2)%4
    x = x + dirList[backdir][0]
    y = y + dirList[backdir][1]
    return x, y


dirCheck = 0
count = 1
print(x, y)
while True:
    print(currentDir, checkleft(x, y, currentDir))
    if checkleft(x, y, currentDir):
        print(f"currentDir = {currentDir}")
        currentDir = rotationleft(currentDir)
        print(f"currentDir = {currentDir}")
        print(x, y)
        gameMap[x][y] = 2
        x, y = go(x, y, currentDir)
        dirCheck = 0
        print(x, y)
        count += 1
    else:
        currentDir = rotationleft(currentDir)
        dirCheck += 1
        if dirCheck == 4:
            if checkback(x, y, currentDir):
                gameMap[x][y] = 2
                x, y = back(x, y, currentDir)
            else:
                break
            dirCheck = 0
        continue

print(count)