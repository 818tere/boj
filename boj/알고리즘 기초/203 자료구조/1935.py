n = int(input())
word = input() # 단어가 아닌 한 글자씩 받아야 함
num_list = [] # 각 알파벳에 대응하는 숫자를 저장할 리스트

for i in range(n):
    num_list.append(int(input())) # 각 알파벳에 대응하는 숫자를 입력받음

stack = [] # result

for i in word:
    if 'A' <= i <= 'Z': # 알파벳이면
        stack.append(num_list[ord(i) - ord('A')]) # 대응하는 숫자를 스택에 저장
    else: # 연산자면
        num2 = stack.pop()
        num1 = stack.pop()
        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        elif i == '/':
            stack.append(num1 / num2)
print('%.2f' % stack[0]) # 소수점 둘째자리까지 출력