def display(li):
    for i in range(len(li)):
        for j in range(len(li[0])):
            print(li[i][j], end=' ')
        print()



def rotation(key):
    newlist = [[0]*len(key) for i in range(len(key[0]))]
    ki = len(key[0])-1
    for i in range(len(newlist)):
        kj = 0
        for j in range(len(newlist[0])):
            newlist[i][j] = key[kj][ki]
            kj += 1
        ki -= 1
    return newlist


def checkkey(key, extendLock, keySize, lockSize, offset):
    realkey = [[1]*lockSize for i in range(lockSize)]

    for i in range(lockSize*2):
        for j in range(lockSize*2):
            testLock = [[0]*len(extendLock) for i in range(len(extendLock[0]))]
            for a in range(len(extendLock)):
                for b in range(len(extendLock[0])):
                    testLock[a][b] = extendLock[a][b]
            for a in range(keySize):
                for b in range(keySize):
                    testLock[a+i][b+j] += key[a][b]
            # display(testLock)
            solvelock = [[0]*lockSize for i in range(lockSize)]
            for a in range(lockSize):
                for b in range(lockSize):
                    solvelock[a][b] = testLock[a+offset[0]][b+offset[1]]

            if solvelock == realkey:
                return True
    return False


def solution(key, lock):
    answer = True
    keySize = len(key)
    lockSize = len(lock)
    extendLock = [[0]*len(lock)*3 for i in range(len(lock)*3)]

    offset = [lockSize, lockSize]
    for i in range(lockSize):
        for j in range(lockSize):
            extendLock[i+offset[0]][j+offset[1]] = lock[i][j]
    count = 0
    while True:
        if checkkey(key, extendLock, keySize, lockSize, offset):
            answer = True
            break
        else:
            count += 1
            if count == 4:
                answer = False
                break
        key = rotation(key)
    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))