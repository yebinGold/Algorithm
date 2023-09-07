def solution(s):
    cnt = 0
    
    while len(s) > 0:
        char = s[0]; s = s[1:]
        same = 1; diff = 0
    
        for x in s:
            if same == diff:
                cnt += 1; break
            if x == char:
                same += 1; s = s[1:]
            else:
                diff += 1; s = s[1:]
    
    return cnt + 1 # 분해 횟수 + 마지막 문자열


"""

문제 조건을 직관적으로 구현했다.

다만 n이 커질수록 슬라이싱이 비효율적일 수 있을 것 같음
리스트로 변환해서 인덱스를 관리하는 게 더 나았으려나

"""
