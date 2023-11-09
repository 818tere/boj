while True:
    try:
        s = input()
        s_list = [0] * 4 # 소문자, 대문자, 숫자, 공백 개수만큼 리스트 생성
        for i in s:
            if i.islower():
                s_list[0] += 1
            elif i.isupper():
                s_list[1] += 1
            elif i.isdigit():
                s_list[2] += 1
            elif i.isspace():
                s_list[3] += 1
        for i in s_list:
            print(i, end=' ')
        print()
    except EOFError:
        break