import sys

datas = sys.stdin.readline().rstrip()
datas = list(map(int, str(datas)))

result = datas[0]
for i in range(1, len(datas)):
    if datas[i] <= 1 or result <= 1:
        result += datas[i]
    else:
        result *= datas[i]

print(result)
