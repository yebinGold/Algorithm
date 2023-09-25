def solution(chicken):
    answer = 0
    left_coupon = 0
    
    while chicken + left_coupon >= 10:
        cp = chicken + left_coupon # 현재 사용 가능한 쿠폰
        chicken = cp // 10 # 주문 가능한 서비스 치킨
        answer += chicken
        left_coupon = cp % 10 # 치킨 주문하고 남은 쿠폰
    
    return answer
