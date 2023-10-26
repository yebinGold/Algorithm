def solution(my_string):
    answer = ""
    used = []
    
    for s in my_string:
        if s in used:
            continue
        used.append(s)
        answer += s
    
    return answer
