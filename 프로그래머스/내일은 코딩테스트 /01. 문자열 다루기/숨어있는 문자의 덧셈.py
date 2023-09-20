def solution(my_string):
    answer = 0
    temp = ""
    
    for s in my_string:
        if s.isnumeric():
            temp += s
            continue
        if len(temp) != 0:
            answer += int(temp)
            temp = ""
    
    if len(temp) != 0:
        answer += int(temp)
    
    return answer
