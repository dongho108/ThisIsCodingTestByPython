def checkfloor(x, y):
    if y == 0:
        return True
    else:
        return False



def checkothercolumn(x, y, answer):
    print("checkothercolumn")
    for i in range(len(answer)):
        if answer[i][2] == 0:
            tx, ty, t = answer[i]
            ty += 1
            # print([x,y], [tx, ty])
            if [x, y] == [tx, ty]:
                return True
    return False

def check1sidebeam(x, y, answer):
    print("check1sidebeam")
    for i in range(len(answer)):
        if answer[i][2] == 1:
            tx, ty, t = answer[i]
            tx1 = tx+1
            # print([x,y], [tx, ty])
            # print([x,y], [tx1,ty])
            if [x, y] == [tx, ty] or [x, y] == [tx1, ty]:
                return True
    return False


def check2sidebeam(x, y, answer):
    print("check2sidebeam")
    checkDouble = 0
    for i in range(len(answer)):
        if [x, x+1] == [answer[i][0], answer[i][0]+1]:
            continue
        if answer[i][2] == 1 and answer[i][1] == y:
            # print(f"x = {x}, answerX = {answer[i][0]} or {answer[i][0]+1}")
            if answer[i][0] == x or answer[i][0]+1 == x:
                checkDouble += 1
    for i in range(len(answer)):
        if [x, x+1] == [answer[i][0], answer[i][0]+1]:
            continue
        if answer[i][2] == 1 and answer[i][1] == y:
            # print(f"x = {x+1}, answerX = {answer[i][0]} or {answer[i][0]+1}")
            if answer[i][0] == x+1 or answer[i][0]+1 == x+1:
                checkDouble += 1
    print(f"checkDouble = {checkDouble}")
    if checkDouble > 1:
        return True
    else:
        return False


def checkcolumn(x, y, answer):
    if checkfloor(x, y) or checkothercolumn(x, y, answer) or check1sidebeam(x, y, answer):
        return True
    else:
        return False


def checkbeam(x, y, answer):
    if checkothercolumn(x, y, answer) or checkothercolumn(x+1, y, answer) or check2sidebeam(x, y, answer):
        return True
    else:
        return False


def checkframe(frame):
    # print(f"len(frame) = {len(frame)}");
    for i in range(len(frame)):
        # print(frame[i][2])
        if frame[i][2] == 0: # 기둥
            if checkcolumn(frame[i][0], frame[i][1], frame):
                print("check1")
                pass
            else:
                return False
        else:
            # print(frame[i][0], frame[i][1])
            if checkbeam(frame[i][0], frame[i][1], frame):
                print("check2")
                pass
            else:
                return False
    return True





def solution(n, build_frame):
    answer = [[]]

    for i in range(len(build_frame)):
        print(f"answer = {answer}")

        x, y, a, b = build_frame[i]

        if not answer[0]: # 맨처음엔 어차피 무조건 들어올 수 있음
            answer[0] = [x, y, a]
            continue
        else:
            frame = [[0]*3 for i in range(len(answer))]

        for j in range(len(answer)):
            for k in range(len(answer[0])):
                frame[j][k] = answer[j][k]


        findIndex = -1
        if b == 0: # delete
            # print("delete")
            # frame에서 x, y, a 찾아서 지우기
            for j in range(len(frame)):
                if frame[j] == [x, y, a]:
                    findIndex = j
            frame.pop(findIndex)
        else:
            # print("insert")
            # frame에 x, y, a 넣기
            frame.append([x, y, a])
        print(f"{i} : init frame = {frame}")

        # true -> answer에 frame 값 넣기
        # false -> answer 변화 x
        # print(frame)
        if checkframe(frame):
            # print("possible !")
            if b == 0:
                answer.pop(findIndex)
            else:
                answer.append([x, y, a])

        else:
            # print("impossible !")
            pass

    answer.sort(key=lambda x:(x[0], x[1]))
    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))