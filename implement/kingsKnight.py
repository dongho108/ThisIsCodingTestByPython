position = list(input())

x = int(position[1])
y = ord(position[0]) - ord('a') + 1

xvec = [-1, -2, -2, -1, 1, 2, 2, 1]
yvec = [-2, -1, 1, 2, 2, 1, -1, -2]

count = 0
for i in range(len(xvec)):
    if x + xvec[i] > 0 and y + yvec[i] > 0:
        count += 1

print(count)