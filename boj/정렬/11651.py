# y좌표가 증가하는 순으로
n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])
arr = sorted(arr)
for i in range(n):
    print(arr[i][1], arr[i][0])