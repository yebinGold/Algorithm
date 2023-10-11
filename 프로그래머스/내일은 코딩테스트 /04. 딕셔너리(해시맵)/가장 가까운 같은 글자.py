def solution(s):
    where = {} # 각 문자별로 가장 마지막에 나온 위치 인덱스 저장
    answer = []
    
    for i, x in enumerate(s):
        if x not in where:
            where[x] = i
            answer.append(-1)
        else:
            answer.append(i - where[x])
            where[x] = i
    
    return answer
