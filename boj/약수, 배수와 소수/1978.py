cnt = int(input())
pnum = 0
nums = list(map(int,input().split())) # 한줄 무제한 입력받아서 리스트로 저장

for n in nums:
    for i in range(2,n+1): # 자기 자신만 약수를 가지는지 확인
        if n % i == 0:
            if n == i:
                pnum += 1
            break
print(pnum)