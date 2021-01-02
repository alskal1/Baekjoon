import sys

a = []
count = 0

for i in range(10):
    n = int(sys.stdin.readline())
    n %= 42
    if n not in a:
        count += 1
    a.append(n)

print(count)