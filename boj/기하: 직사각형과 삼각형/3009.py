list_x = []
list_y = []
for _ in range(3):
    x, y = map(int, input().split()) # 두 개를 한줄씩 세 번 입력받아
    list_x.append(x)
    list_y.append(y)

for i in range(3):
    if list_x.count(list_x[i]) == 1:
        x = list_x[i]
    if list_y.count(list_y[i]) == 1:
        y = list_y[i]
print(x, y)