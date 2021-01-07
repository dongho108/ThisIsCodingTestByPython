data = input()

continueNum = [0, 0]
continueNum[int(data[0])] += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        continueNum[int(data[i+1])] += 1

print(min(continueNum[0], continueNum[1]))
