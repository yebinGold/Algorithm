# 2023 KAKAO BLIND RECRUITMENT 기출문제
def solution(today, terms, privacies):
    answer = []
    
    # 약관 종류: 유효 기간
    dict = {term[0]: int(term[2:]) for term in terms}
    
    # 오늘 날짜
    ny, nm, nd = map(int, today.split("."))
    td = ((ny * 12 + nm) * 28) + nd
    
    for i in range(len(privacies)):
        date, term = privacies[i].split(" ")
        y, m, d = map(int, date.split("."))
        
        # 파기 예정일
        date = ((y * 12 + m + dict[term]) * 28) + d - 1
        
        if date < td:
            answer.append(i+1)
        
    return answer

"""

1. terms 배열을 조회가 쉽도록 딕셔너리 형태로 변환했다.
2. 모든 달은 28일까지 있다고 가정하는 조건을 이용하여 입력받은 날짜 정보를 년.월.일에서 일 단위로 바꾼다.
  - 이때 개인정보 파기 예정일을 구하는 과정에서 월 단위 계산을 하고 나서 1일을 빼줘야 함에 유의
3. 오늘 날짜와 개인정보 유효기간을 비교하며 파기할 정보의 개수를 센다.

"""
