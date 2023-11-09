n = int(input())
for i in range(1, n): #가장 작은 생성자 찾기
    if i + sum(map(int, str(i))) == n:
        print(i)
        exit()
print(0)