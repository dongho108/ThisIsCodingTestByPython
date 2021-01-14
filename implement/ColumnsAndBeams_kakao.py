def checkfloor(x, y):
    if y == 0:
        return True
    else:
        return False



def checkothercolumn(x, y, answer):
    for i in range(len(answer)):
        if answer[i][2] == 0:
            tx, ty, t = answer[i]
            tx += 1
            print([x,y], [tx, ty])
            if [x, y] == [tx, ty]:
                return True
    return False

def check1sidebeam(x, y, answer):
    for i in range(len(answer)):
        if answer[i][2] == 1:
            tx, ty, t = answer[i]
            tx1 = tx+1
            print([x,y], [tx, ty])
            print([x,y], [tx1,ty])
            if [x, y] == [tx, ty] or [x, y] == [tx1, ty]:
                return True
    return False


def check2sidebeam(x, y, answer):
    for i in range(len(answer)):
        if answer[i][2] == 1:
            tx, ty, t = answer[i]
            tx1 = tx+1
            print([x,y], [tx, ty])
            print([x,y], [tx1,ty])
            if [x, y] == [tx, ty] and [x, y] == [tx1, ty]:
                return True
    return False


def checkcolumn(x, y, answer):
    if checkfloor(x, y) or checkothercolumn(x, y, answer) or check1sidebeam(x, y, answer):
        return True
    else:
        return False


def checkbeam(x, y, answer):
    if checkothercolumn(x, y, answer) or checkothercolumn(x, y+1, answer) or check2sidebeam(x, y, answer):
        return True
    else:
        return False




def installcolumn(x, y, answer):
    check = checkcolumn(x, y, answer)
    if check == True:
        return [x, y, 0]
    else:
        return [-1, -1, 0]


def installbeam(x, y, answer):
    check = checkbeam(x, y, answer)
    if check == True:
        return [x, y, 1]
    else:
        return [-1, -1, 1]


def deletecolumn(x, y, answer):
    check = checkframe(frame)
    if check == True:
        deletecolumn

def deletebeam(x, y, answer):


def solution(n, build_frame):
    answer = [[]]

    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]

        frame = [[0]*len(answer) for i in range(len(answer))]
        for i in range(len(answer)):
            for j in range(3):
                frame[i][j] = answer[i][j]

        if b == 0: # delete
            # frame에서 x, y, a 찾아서 지우기
        else:
            # frame에 x, y, a 넣기

        # checkframe(frame)
        # true -> answer에 frame 값 넣기
        # false -> answer 변화 x





    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))