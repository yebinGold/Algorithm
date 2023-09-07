# 테케 통과 O 채점 통과 X

def solution(citations):
    citations.sort()
    n = len(citations) # 논문 개수
    h = (citations[0] + citations[n - 1]) // 2 # 중간값에서 시작
    answer = 0
    
    while n >= h:
        if citations[-h] >= h:
            answer = h
            h += 1
        else:
            h -= 1
            if answer == h:
                return answer
    
    return answer

"""
논문 최소 인용 횟수와 최대 인용 횟수의 중간 값(=h)에서부터 탐색을 시작한다.

H-Index의 정의 = "h번 이상 인용된 논문이 h편 이상인 값 h의 최댓값" 이므로
배열 오름차순 정렬 후 뒤에서부터 h번째 논문의 인용 횟수를 값 h와 비교하는 것으로 H-Index 여부를 확인했다. 

현재 h가 H-Index가 될 수 있으면 일단 answer 후보로 놓고 가능한 더 큰 값을 찾기 위해 h를 1 늘려서 추가 검사를 진행했다.

만약 h가 H-Index가 될 수 없다면 h를 1 낮춰서 가능한 다른 후보를 탐색했다.
이때, (-1)한 h 값이 현재 가능한 H-Index의 최댓값이라면 정답을 그대로 반환했다.


기존 + 추가 테스트케이스는 모두 통과 but 틀림
다른 반례를 찾아서 디버깅을 해줘야겠다. 당장은 뭐가 문제인지 모르겠음..
"""
