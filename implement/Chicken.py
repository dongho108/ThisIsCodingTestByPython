from itertools import combinations


def Cal_distance():
    return

n, m = map(int, input().split())

city = []
chickenList = []
homeList = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in city[i]:
        if j == 2:
            chickenList.append([i, j])
        if j == 1:
            homeList.append([i, j])


pickChickenList = list(combinations(chickenList, m))
print(pickChickenList)

result = []
for pickChicken in pickChickenList:
    semiresult = []
    for chicken in pickChicken:




