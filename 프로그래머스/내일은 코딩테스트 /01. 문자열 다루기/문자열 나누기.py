def solution(s):
    answer = 0
    s = list(s)
    
    while len(s) > 0:
        x = s[0]; s.pop(0)
        same = 1; diff = 0
        
        while len(s) > 0:
            if same == diff:
                answer += 1
                break
            if x == s[0]:
                same += 1
            else:
                diff += 1
            s.pop(0)  
    
    return answer + 1
