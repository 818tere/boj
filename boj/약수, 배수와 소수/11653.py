n = int(input())
if n == 1:
    exit()

for i in range(2, n+1):
    while n % i == 0:
        print(i)
        n //= i
    if n == 1:
        break