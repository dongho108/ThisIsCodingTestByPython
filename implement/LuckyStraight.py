n = list(input())

half = len(n) // 2
left = 0
right = 0
for i in range(half):
    left += int(n[i])
    right += int(n[half+i])

if left == right:
    print("LUCKY")
else:
    print("READY")




