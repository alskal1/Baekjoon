import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
sum = str(A*B*C)

for i in range(10):
    count = sum.count(str(i))
    print(count)