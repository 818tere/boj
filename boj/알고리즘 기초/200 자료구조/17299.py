from collections import Counter

n = int(input())
a = list(map(int, input().split()))
stack = [] # stack에는 a의 인덱스가 들어감
result = [-1 for _ in range(n)]
a_count = Counter(a) # a의 각 원소의 개수를 세서 딕셔너리로 만듦
print(a_count)
for i in range(n):
    try: # stack이 비어있지 않으면
        while a_count[a[stack[-1]]] < a_count[a[i]]:
            result[stack.pop()] = a[i]
    except: # stack이 비어있으면
        pass
    stack.append(i)

for i in range(n):
    print(result[i], end=' ')