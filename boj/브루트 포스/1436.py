# hint: 1부터 10,000까지의 숫자 중에서'666'이 들어간 숫자를 찾고 그 숫자가 몇 번째 숫자인지 출력
# 브루트 포스: 암호학에서 시작하여 알고리즘에서는 1부터 모든 수를 대입해보는 것을 의미
n = int(input())
num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1 #666 667 668 ... 1666일 때 cnt = 2 2666

