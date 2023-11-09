# x좌표가 증가하는 순으로
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr)
for i in range(n):
    print(arr[i][0], arr[i][1])