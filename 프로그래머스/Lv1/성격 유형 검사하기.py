# 2022 KAKAO TECH INTERNSHIP 기출문제
def solution(survey, choices):
    # 각 지표별 성격 유형이 사전순으로 나열되어 있는 딕셔너리
    result = {"R": 0, "T": 0,"C": 0,"F": 0,"J": 0,"M": 0,"A": 0,"N": 0}
    
    for q, a in zip(survey, choices):
        score = abs(4 - a)
        
        # 비동의 관련 선택지
        if a < 4:
            result[q[0]] += score
        # 동의 관련 선택지
        elif a > 4:
            result[q[1]] += score
    
    # 검사 결과 반환
    answer = ""
    items = list(result.items())
    
    for i in range(0, 7, 2): # 0, 2, 4, 6
        if items[i][1] >= items[i+1][1]:
            answer += items[i][0]  
        else:
            answer += items[i+1][0]
    
    return answer

"""

8가지 성격 유형과 해당 유형의 점수를 딕셔너리로 저장하고,
최종적으로 4가지 지표 순서대로 각각 점수를 비교하여 검사 결과를 얻었다.

비교 대상의 개수가 한정적이어서 하드코딩한 부분이 몇 군데 있지만 간단하게 풀이 완료!

"""
