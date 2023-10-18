def solution(participant, completion):
    answer = 0
    htable = {}
    
    for p in participant:
        answer += hash(p)
        htable[hash(p)] = p
    for c in completion:
        answer -= hash(c)
    
    return htable[answer]
