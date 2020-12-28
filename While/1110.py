
n = x = int(input())
count = 0
while True:
    a = n // 10
    b = n % 10
    sum = a + b
    count += 1
    n = int(str(n % 10) + str(sum % 10))

    if n == x:
        break

print(count)