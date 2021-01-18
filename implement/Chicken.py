from itertools import combinations


def Cal_distance(home, chicken):
    return abs(home[0]-chicken[0]) + abs(home[1]-chicken[1])

n, m = map(int, input().split())

city = []
chickenList = []
homeList = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 2:
            chickenList.append([i, j])
        if city[i][j] == 1:
            homeList.append([i, j])


pickChickenList = list(combinations(chickenList, m))
# print(pickChickenList)
# print(homeList)

results = []

for pickChicken in pickChickenList:
    semiResult = 0
    for home in homeList:
        eachHome = []
        for chicken in pickChicken:
            # print(home, chicken)
            eachHome.append(Cal_distance(home, chicken))
        # print(f"eachHome = {eachHome}, min = {min(eachHome)}")
        semiResult += min(eachHome)
    results.append(semiResult)

# print(results)
print(min(results))

