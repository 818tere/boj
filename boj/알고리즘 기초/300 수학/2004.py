# 진짜 팩토리얼로 구해서 문제를 풀면 시간초과가 난다.
# 끝자리가 0이라는 것은 2와 5의 곱으로 이루어진다는 것이다.
# 2와 5의 짝이 맞아야 10이 되므로 2의 개수와 5의 개수 중 더 작은 것이 10의 개수가 된다.

n, m = map(int, input().split())

def count(n, k): # n!에서 k의 개수를 세는 함수
    cnt = 0
    while n != 0:
        n //= k
        cnt += n
    return cnt

five_count = count(n, 5) - count(m, 5) - count(n-m, 5)
two_count = count(n, 2) - count(m, 2) - count(n-m, 2)

print(min(five_count, two_count))