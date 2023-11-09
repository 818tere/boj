#메모리 제한이 적어서 sort 사용 불가
#따라서 미리 배열의 크기를 정해주고 인덱스를 활용해야한다.
import sys

n = int(input()) #(1 ≤ N ≤ 10,000,000) 
arr = [0] * 10001 # 1 ≤ arr[i] ≤ 10,000

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1 

for i in range(10001):
    if arr[i] != 0: #카운트가 된 것만
        for j in range(arr[i]): # 인덱스 순서대로 출력
            print(i)