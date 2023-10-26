def solution(survey, choices):
    answer = ''
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for q, a in zip(survey, choices):
        if a < 4:
            score[q[0]] += abs(4 - a)
        elif a > 4:
            score[q[1]] += abs(4 - a)
    
    result = list(score.items())
    
    for i in range(0, 7, 2):
        if result[i][1] >= result[i+1][1]:
            answer += result[i][0]
        else:
            answer += result[i+1][0]
    
    return answer
