t = int(input())

for _ in range(t):
    stack = []
    sentence = input()
    for i in sentence:
        if i == '(': #여는 괄호는 스택에 넣기
            stack.append(i)
        elif i == ')': #닫는 괄호는 스택에서 빼기
            if len(stack) == 0: #스택이 비어있으면 NO
                stack.append(i)
                break
            else:
                stack.pop() 
    if len(stack) == 0: 
        print('YES')
    else:
        print('NO')