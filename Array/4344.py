import sys

C = int(sys.stdin.readline())
for i in range(C):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    count = 0
    for i in num[1:]:
        if i > avg:
            count += 1
        rate = count / num[0] * 100
    print("%.3f" %rate + "%")