import sys
input = sys.stdin.readline

n = int(input())
deque = []
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        deque.insert(0, command[1]) # insert(인덱스, 값)
    elif command[0] == 'push_back':
        deque.append(command[1]) # append(값)
    elif command[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop(0)) # pop(인덱스)
    elif command[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop()) # pop()
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0]) 
    elif command[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])