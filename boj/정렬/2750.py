n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort() #배열의 정렬을 이용
for i in arr:
    print(i)