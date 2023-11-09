import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push': #[0]은 push, [1]은 숫자
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) #스택 가장 위에 있는 원소 출력(마지막 원소)