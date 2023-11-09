word = input()
stack = []
result = ''

for x in word:
    if x.isalpha():
        result += x
    else: # 연산자
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/': # 우선순위가 높은 연산자
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop() 
            stack.append(x) # 스택에 넣기
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # '(' 제거
while stack:
    result += stack.pop()
    
print(result)