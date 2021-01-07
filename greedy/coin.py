n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += 1
    n %= coin

print(count)