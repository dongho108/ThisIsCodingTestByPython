n, k = map(int, input().split())
count = 0


# solution 1

# while n != 1:
#     if n%k == 0:
#         n /= k
#     else:
#         n -= 1
#     count += 1



# solution 2

while True:
    target = (n // k) * k
    count += (n-target)
    n = target
    if n < k:
        break

    n //= k
    count += 1

count += n
count -= 1

print(count)
