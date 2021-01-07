from collections import Counter

n, m = map(int, input().split())
data = list(map(int, input().split()))

overlap = Counter(data)
count=0;
print(overlap[4])
for i in range(1, m+1):
    if overlap[i] >= 2:
        count += 1
result = n*(n-1)//2 - count
print(result)