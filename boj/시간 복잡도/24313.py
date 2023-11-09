a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())
f = a1*n0 + a0
for i in range(n0, 100):
    f = a1*i + a0
    if f > c*i:
        print(0)
        exit()
print(1)