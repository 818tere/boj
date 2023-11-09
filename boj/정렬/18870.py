# 값을 비교해 순서대로 정렬한 후, 인덱스를 뽑아내라
n = int(input())
arr = list(map(int, input().split())) # 한 줄 입력
arr2 = sorted(list(set(arr))) # 중복 제거한 후 정렬
dic = {arr2[i]: i for i in range(len(arr2))} # 인덱스 입력
for i in arr:
    print(dic[i], end=' ') # 인덱스 출력