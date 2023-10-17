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
