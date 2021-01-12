def solution(s):
    s = list(s)
    result = [len(s)] * (len(s) // 2 + 1)
    for i in range(1, (len(s) // 2 + 1)):
        print(f"i = {i}")
        pre = ''
        now = ''
        ctnCnt = 1
        for j in range(0, len(s), i):
            now = ''
            for k in range(i):
                if j+k > len(s)-1:
                    break
                now += s[j + k]
            if pre == now:
                ctnCnt += 1
            else:
                if ctnCnt > 1:  # 이 전이 연속이었을때
                    print(pre, now, result[i])
                    print(result[i], i, ctnCnt)
                    result[i] = result[i] - (i * ctnCnt) + i + len(str(ctnCnt))
                    print(pre, now, result[i])
                    print("----")
                ctnCnt = 1
            pre = now
        if ctnCnt > 1:  # 이 전이 연속이었을때 마지막꺼
            print(pre, now, result[i])
            print(result[i], i, ctnCnt)
            result[i] = result[i] - (i * ctnCnt) + i + len(str(ctnCnt))
            print(pre, now, result[i])
            print("----")

    print(result)
    answer = min(result)
    return answer

print(solution(input()))
