# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써 하나의 수열을 만들어야.
n = int(input())
stack = [] # 수열 생성
result = [] # +, - 기호 저장
count = 1 # 1부터 n까지의 수를 오름차순으로 push
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))