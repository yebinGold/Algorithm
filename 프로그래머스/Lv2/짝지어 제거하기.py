def solution(s):
    chars = []
  
    # 스택 자료구조를 활용해서 문자열 짝을 순차적으로 제거
    for x in s:
        if len(chars) != 0 and chars[-1] == x:
            chars.pop()
        else:
            chars.append(x)

    return 1 if len(chars) == 0 else 0
