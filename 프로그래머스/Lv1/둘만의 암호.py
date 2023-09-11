def solution(s, skip, index):
    answer = ''
    
    for x in s:
        cnt = 0
        temp = ord(x)
        
        while cnt < index:
            if temp == ord("z"):
                temp = ord("a") - 1
                
            if chr(temp + 1) in skip:
                temp += 1
                continue
            else:
                temp += 1
                cnt += 1
        
        answer += chr(temp)

    return answer

"""

알파벳 소문자 배열을 갖다가 사용할까도 고려해봤지만,
주어지는 입력 크기가 작아서 그냥 단순하게 바꾸려는 모든 문자를 하나씩 살펴보는 코드를 작성했다.

"""
