n = int(input())
a = list(map(int, input().split())) # 띄어쓰기로 받은 값을 int()하고 리스트로 저장
stack = [] # stack에는 a의 인덱스가 들어감
result = [-1 for _ in range(n)] # -1로 초기화된 리스트 생성

for i in range(n):
    try: # stack이 비어있지 않으면
        while a[stack[-1]] < a[i]: # stack의 마지막 값이 a[i]보다 작으면
            result[stack.pop()] = a[i] # result의 stack의 마지막 값을 a[i]로 바꾼다.
    except: # stack이 비어있으면
        pass
    stack.append(i)
for i in range(n):
    print(result[i], end=' ') # result 출력