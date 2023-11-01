def solution(s, skip, index):
    alpha = list(filter(lambda x: x not in skip, ascii_lowercase))
    answer = ''
    
    for x in s:
        idx = alpha.index(x) + index
        if idx < len(alpha):
            answer += alpha[idx]
        else:
            answer += alpha[idx - len(alpha)]
        
    return answer


"""
런타임 에러 3 17 18 19
"""
