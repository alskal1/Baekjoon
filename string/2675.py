
T = int(input())

for i in range(T):
    R, S = input().split()
    P = ''
    for i in S:
        sum = i * int(R)
        P += sum
    print(P)