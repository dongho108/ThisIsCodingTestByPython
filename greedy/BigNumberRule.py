n, m, k = map(int, input().split())
data = list(map(int, input().split()))

first = data.pop(data.index(max(data)))
second = data.pop(data.index(max(data)))

firstNum = (m // (k+1)) * k
secondNum = firstNum//k + (m % (k+1))

result = first * firstNum + second * secondNum
print(result)



