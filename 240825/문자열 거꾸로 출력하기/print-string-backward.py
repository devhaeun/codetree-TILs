while True:
    string = input()
    if string == 'END':
        break
    # 문자열 거꾸로 뒤집어 출력
    result = string[-1::-1]
    print(result)