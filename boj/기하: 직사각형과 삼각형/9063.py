n = int(input())
list_x = []
list_y = []
for _ in range(n):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)
print((max(list_x)-min(list_x))*(max(list_y)-min(list_y)))