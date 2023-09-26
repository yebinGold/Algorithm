def solution(array):
    answer = 0
    for x in array:
        answer += str(x).count('7')
        
    return answer
