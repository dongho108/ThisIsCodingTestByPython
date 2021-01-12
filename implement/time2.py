n, k = map(int, input().split())


def checkFunc (hour, minute, second):
    hourlist = list(str(hour))
    if hour < 10:
        hourlist.append('0')
    minutelist = list(str(minute))
    if minute < 10:
        minutelist.append('0')
    secondlist = list(str(second))
    if second < 10:
        secondlist.append('0')

    target = str(k)
    if target in hourlist or target in minutelist or target in secondlist:
        return 1
    else:
        return 0


count = 0

for hour in range(24):
    for minute in range(60):
        for second in range(60):
            check = checkFunc(hour, minute, second)
            count += check
    if hour == n:
        break

print(count)


