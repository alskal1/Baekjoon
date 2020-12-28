import sys

T = int(sys.stdin.readline())
x = 0

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    x += 1
    print("Case #%s: %s + %s = %s"%(x, a, b, a+b))