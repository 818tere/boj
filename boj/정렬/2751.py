#input() 이 sys.stdin.readline() 보다 느린 이유 :
#input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
#개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
import sys

n = int(input()) #(1 ≤ N ≤ 1,000,000) 
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline())) 
arr.sort()
for i in arr:
    print(i)