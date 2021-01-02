import sys

N = int(sys.stdin.readline())
score = list(map(int, input().split()))
best = max(score)
sum = 0

for i in range(N):
    sum += score[i]/best*100

print(sum/N)

