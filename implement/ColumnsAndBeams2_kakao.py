def checkframe(frame):
    for x, y, a in frame:
        if a == 0:
            if y == 0 or [x, y-1, 0] in frame or [x-1, y, 1] in frame or [x, y, 1] in frame:
                continue
            else:
                return False
        elif a == 1:
            if [x, y-1, 0] in frame or [x+1, y-1, 0] in frame or ([x-1, y, 1] in frame and [x+1, y, 1] in frame):
                continue
            else:
                return False
    return True



def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            answer.remove([x, y, a])
            if not checkframe(answer):
                answer.append([x, y, a])

        elif b == 1:
            answer.append([x, y, a])
            if not checkframe(answer):
                answer.remove([x, y, a])

    return sorted(answer)

    # answer.sort(key=lambda x:(x[0], x[1]))
    # return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))