t = int(input())
stack = []
for _ in range(t):
    sentence = input().split()
    for i in sentence:
        stack.append(i[::-1]) #문자열 뒤집은 것을 리스트에 넣기
print(' '.join(stack)) #리스트를 문자열로 바꾸기