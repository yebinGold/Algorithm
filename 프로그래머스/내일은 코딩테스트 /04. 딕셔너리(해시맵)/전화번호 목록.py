# 1) brute force - 정확성 테스트 통과 / 효율성 테스트 실패
def solution(phone_book):
    phone_book = sorted(phone_book)
    l = len(phone_book)
    
    if l <= 1:
        return True
    
    for i in range(l-1):
        a = phone_book[i]
        for b in phone_book[i+1:]:
            if b.startswith(a):
                return False
    
    return True


#2) 슬라이싱 -> 인덱스를 관리하는 방식으로 수정 - 똑같이 효율성 테스트 3, 4번 타임아웃
def solution(phone_book):
    (...)
    
    for i in range(l-1):
        a = phone_book[i]
        
        # 리스트 슬라이싱 -> range 객체
        for j in range(i+1, l):
            b = phone_book[j]
            if b.startswith(a):
                return False
    
    return True
