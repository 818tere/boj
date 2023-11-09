import sys
input = sys.stdin.readline().rstrip

s = input()
stack = []
result = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else: # 두 가지 경우로 나뉜다
        stack.pop()
        if s[i-1] == '(': # 레이저인 경우
            result += len(stack) # 현재 stack에 쌓인 '('의 개수만큼 더해준다
        else: # 쇠막대기의 끝인 경우
            result += 1 # 하나만 더해준다
print(result)