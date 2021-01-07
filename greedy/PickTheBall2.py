n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0]*11

for i in data:
    array[i] += 1

result = 0
for i in range(1, m+1):
    n = n - array[i]
    result = result + array[i] * n

print(result)