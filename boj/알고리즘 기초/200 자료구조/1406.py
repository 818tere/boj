import sys
input = sys.stdin.readline

stack_l = list(input().rstrip()) #커서를 가운데 둔다고 가정하고 왼쪽 스택에 문자들을 저장
stack_r = [] #커서 기준으로 오른쪽 스택

n = int(input())
for _ in range(n):
    command = input().split() 
    if command[0] == 'L':
        if stack_l: 
            stack_r.append(stack_l.pop()) 
    elif command[0] == 'D': #커서를 오른쪽으로 한 칸 이동인데
        if stack_r: #커서 왼쪽에 값이 있으면
            stack_l.append(stack_r.pop())  #오른쪽 스택에서 왼쪽 스택으로 이동
    elif command[0] == 'B':
        if stack_l: 
            stack_l.pop() #그냥 왼쪽 스택에서 pop하면 된다
    elif command[0] == 'P': 
        stack_l.append(command[1]) #P 뒤에 오는 문자를 커서 왼쪽에 추가
print(''.join(stack_l + list(reversed(stack_r)))) #커서 왼쪽에 있는 문자들을 뒤집어서 출력
