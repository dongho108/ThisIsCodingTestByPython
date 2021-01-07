import heapq

def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    q=[]

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    for i in range(length):
        if sum_value + ((q[0][0] - previous) * length) <= k:
            now = heapq.heappop(q)[0] # 다 먹은 음식 시간
            sum_value += (now - previous) * length
            length -= 1
            previous = now
        else:
            break

    print(q)
    result = sorted(q, key=lambda x: x[1])
    print(result)

    answer = result[(k-sum_value) % length][1]
    return answer

print(solution([2, 3, 4], 8))
