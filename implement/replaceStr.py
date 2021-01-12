s = list(input())

num = 0
slist = []
for i in range(len(s)):
    if 47 < ord(s[i]) < 58: # number
        num += int(s[i])
    elif 96 < ord(s[i]) < 123 or 64 < ord(s[i]) < 91:
        slist.append(s[i])

slist.sort()
# for i in range(len(slist)):
#     print(slist[i], end='')
print(''.join(slist), end='')
print(num)

# K1KA5CB7
# AJKDLSI412K4JSJ9D