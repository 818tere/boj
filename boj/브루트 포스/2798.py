n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            s = nums[i] + nums[j] + nums[k]
            if s <= m:
                ans = max(ans, s) #반복해서 m을 넘지 않는 최대값을 찾는다
print(ans)