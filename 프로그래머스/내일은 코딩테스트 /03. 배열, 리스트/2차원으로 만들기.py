def solution(num_list, n):
    answer = []
    temp = []
    
    for i, x in enumerate(num_list):
        temp.append(x)
        if len(temp) == n:
            answer.append(temp)
            temp = []
            
    if len(temp) > 0:
        answer.append(temp)
    
    return answer
