s = input()
alpha = [0] * 26 # 알파벳 개수만큼 리스트 생성
for i in s:
    alpha[ord(i)-97] += 1 # 알파벳 개수 세기
for i in alpha:
    print(i, end=' ')