# 2021 KAKAO BLIND RECRUITMENT 기출문제

import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub("[^a-z0-9\-_.]", "", new_id)
    
    # 3단계
    new_id = re.sub("[\.]{2,}", ".", new_id)
    
    # 4단계
    new_id = re.sub("^[\.]|[\.]$", "", new_id)
    
    # 5단계
    if len(new_id) == 0:
    	new_id = "a"
    
    # 6단계
    if len(new_id) >= 16:
        new_id = re.sub("[\.]$", "", new_id[:15])
    
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id

"""

처음엔 정규식 없이 단계별로 처리하다가, 코드를 깔끔하고 간단하게 작성하기 위해서 오랜만에 정규식을 사용해봤다.

re.sub(pattern, 치환할 문자열, 문자열)

2단계 : a-z(알파벳 소문자), 0-9(숫자), - _ .을 제외(^)한 모든 문자 제거
3단계 : 마침표(.)가 2회 이상 반복될 경우({2, }), 마침표 한 개로 치환
4단계 : 마침표(.)가 맨 앞에(^) 또는 맨 뒤에($) 있는 경우 제거

"""
