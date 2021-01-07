from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

li = [0 for i in range(sum(data)+1)] # 0~16

for i in range(1, n):
    results = list(permutations(data, i))
    for result in results:
        li[sum(result)] = 1
answer = 0
for i in range(1, len(li)):
    if li[i] != 1:
        answer = i
        break
if answer == 0:
    answer = len(li)
print(answer)

