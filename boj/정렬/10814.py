n = int(input())
arr = []
for i in range(n):
    age, name = input().split()
    arr.append([int(age), name])

arr.sort(key=lambda x: x[0]) # (age, name)의 age를 기준으로 정렬
# 파이썬은 기본적으로 stable sort를 사용하기 때문에 같은 값이면 들어온 순서대로 정렬됨
for i in arr:
    print(i[0], i[1])