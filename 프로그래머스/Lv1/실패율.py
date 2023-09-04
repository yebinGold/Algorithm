# 2019 KAKAO BLIND RECRUITMENT 기출문제

def solution(N, stages):
    answer = [0] * (N+2)
    for stage in stages:
        answer[stage] += 1
        
    for i in range(1, N+1):
        all = sum(answer[i:]) # 스테이지에 도달한 플레이어 수
        if not all: 
            rate = 0
        else:
            rate = answer[i] / all
        answer[i] = (i, rate) # (스테이지, 실패율)
    
    answer = answer[1:-1]
    answer.sort(key = lambda x: (-x[1], x[0]))
    
    return [x[0] for x in answer]


# (스테이지 넘버, 실패율)을 투플 형태로 저장.
# sort와 익명 함수 lambda를 사용해서 조건대로 정렬한 후에 넘버에 해당하는 값만 뽑아내서 return했다.

# 뭔가 플레이어 수를 구하는 과정에서 더 효율적인 방법이 있을 것 같은데 일단 통과
