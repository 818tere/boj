n, k = map(int, input().split())
cnt = 0 # cnt번째 약수
for i in range(1, n+1):
    if n % i == 0: #그 약수는 i
        cnt += 1
        if cnt == k:
            break
print(0 if cnt < k else i)