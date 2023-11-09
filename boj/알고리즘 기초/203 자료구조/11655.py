s = input()
result = ''
for i in s:
    if i.isupper():
        if ord(i) + 13 > 90: # ord('Z') == 90
            result += chr(ord(i) - 13) # chr(65) == 'A'
        else:
            result += chr(ord(i) + 13)
    elif i.islower():
        if ord(i) + 13 > 122: # ord('z') == 122
            result += chr(ord(i) - 13) # chr(97) == 'a'
        else:
            result += chr(ord(i) + 13)
    else: # 숫자나 공백은 그대로 출력
        result += i
print(result)