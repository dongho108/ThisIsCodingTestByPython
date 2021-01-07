def solution(food_times, k):
    answer = 0
    time = 0

    while True:
        checkfinish = 0
        while True:
            if checkfinish >= len(food_times):
                answer = -1
                break
            checkfinish += 1
            if answer >= len(food_times):
                answer = 0
            if food_times[answer] != 0:
                break
            else:
                answer += 1
        if time == k or answer == -1:
            break

        food_times[answer] -= 1
        answer += 1
        time += 1

    if answer != -1:
        answer += 1
    return answer

print(solution([3, 1, 2], 5))