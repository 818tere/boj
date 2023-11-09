m = int(input())
n = int(input())
prime = []
for i in range(m, n+1):
    cnt = 0 #약수의 개수
    for j in range(1, i+1): #1부터 자기자신까지
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        prime.append(i)

if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)