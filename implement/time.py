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


hour = 0
minute = 0
second = 0
count = 0

result = [[[0 for a in range(60)] for b in range(60)] for c in range(24)]


for chour in range(24):
    minute = 0
    for cminute in range(60):
        second = 0
        for csecond in range(60):
            result[hour][minute][second] = checkFunc(hour, minute, second)
            count += result[hour][minute][second]
            # if result[hour][minute][second] == 1:
            #     print(hour, minute, second)
            second += 1
        # print(count)
        minute += 1
    if hour == n:
        break
    # print(count)
    hour += 1


# for chour in range(n):
#     for cminute in range(60):
#         for csecond in range(60):
#             print(result[chour][cminute][csecond], end=' ')
#         print("----")
#     print("----------------------")

print(count)


