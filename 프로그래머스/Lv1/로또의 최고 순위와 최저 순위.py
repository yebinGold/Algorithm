# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 기출문제

def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6} # 맞은 개수: 순위
    got = 0 # 실제로 맞은 숫자 개수
    unknown = 0 # 모르는 숫자 개수
    
    for num in lottos:
        if num == 0: unknown += 1
        elif num in win_nums: got += 1
        
    return [rank[got + unknown], rank[got]]


"""
최고 순위 = 실제로 맞은 숫자 + 모르는 숫자가 전부 맞았을 경우
최저 순위 = 실제로 맞은 숫자 + 모르는 숫자가 전부 틀렸을 경우

번호 개수 세서 몇 위인지 체크하면 끝!
"""
