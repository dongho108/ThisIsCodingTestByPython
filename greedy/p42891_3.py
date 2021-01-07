import heapq

def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        return -1

    q=[]

    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    for i in range(len(food_times)):
        if q[0][0] * len(food_times) <= k:
            k -= q[0][0] * len(food_times)
            heapq.heappop(q)
        else:
            break


    result = sorted(q, key=lambda x: x[1])
    answer = result[k % len(q)][1]
    return answer

print(solution([2, 3, 4], 8))