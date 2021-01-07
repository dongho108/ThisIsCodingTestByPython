n = int(input())
data = input().split()

# 동 서 남 북 = 0 1 2 3 = R L D U
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move_type = ['R', 'L', 'D', 'U']


result = [1, 1]

for i in range(len(data)):
    for j in range(len(move_type)):
        if data[i] == move_type[j]:
            x = j
    nx = result[0] + dx[x]
    ny = result[1] + dy[x]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    result[0], result[1] = nx, ny

print(result[0], result[1])