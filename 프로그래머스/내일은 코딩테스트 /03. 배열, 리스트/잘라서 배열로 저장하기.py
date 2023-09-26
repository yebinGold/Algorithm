def solution(my_str, n):
    answer = []
    temp = ""
    
    for i, s in enumerate(my_str):
        temp += s
        if len(temp) == n:
            answer.append(temp)
            temp = ""
            
    if len(temp) > 0:
        answer.append(temp)
    
    return answer
