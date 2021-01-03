import sys

T = int(sys.stdin.readline())

for i in range(T):
    s = sys.stdin.readline()
    score = 0
    sum = 0
    for i in s:
        if i == 'O':
            score += 1
            sum += score
        elif i == 'X':
            score = 0
    print(sum)