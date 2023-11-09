import sys
input = sys.stdin.readline
n, k = map(int, input().split())

queue = [i for i in range(1, n+1)]
result = []

num = 0 # 제거될 사람의 인덱스 번호

for _ in range(n):
    num += k-1
    if num >= len(queue): # 한바퀴를 돌고 그 다음으로 돌아올 때 인덱스가 리스트 길이보다 커질 수 있음
        num = num % len(queue)
    result.append(str(queue.pop(num))) 
print("<", ", ".join(result)[:], ">", sep='') # join은 리스트의 요소들을 합쳐서 하나의 문자열로 만들어줌