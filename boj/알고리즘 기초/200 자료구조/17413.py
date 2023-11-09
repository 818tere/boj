import sys
input = sys.stdin.readline().rstrip
# sys.stdin.readline()은 개행문자를 포함하므로 rstrip()을 통해 제거해준다.

s = input()
tag = False
word = '' # 단어를 저장할 변수
result = '' # 최종 문장을 저장할 변수
for i in s:
    if i == '<':
        tag = True
        result += word[::-1] + '<' # 단어를 뒤집어서 저장해준다.
        word = ''
    elif i == '>':
        tag = False
        result += '>'
    elif tag:
        result += i
    elif i == ' ':
        result += word[::-1] + ' '
        word = ''
    else:
        word += i # 단어를 저장하기 위해서 word에 문자를 추가해준다.
result += word[::-1] # 태그나 띄어쓰기가 없으면 그대로 for문이 종료되므로 저장된 마지막 단어가 있으면 뒤집어서 저장해준다. result에 추가해준다.
print(result)

# input(): 단순하게 문자열 입력받기 class 'str'
# .split(): 문자열을 공백을 기준으로 나누어 리스트로 리턴 class 'list'

# map(함수, 값): 요소를 지정된 함수로 처리해주는 함수
